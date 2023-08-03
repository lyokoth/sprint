#Import libraries
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import base64

from dash import Dash, dcc, html, Input, Output


data = (
    pd.read_csv('csv/200M_Male.csv')
   
    .query("nat == 'USA'")
    .sort_values(by="mark")
)

app = Dash(__name__, external_stylesheets=['/assets/css/dashboard.css'])


app.layout = html.Div(
    children=[
    html.H1(children="Men's Outdoor 200 Meter Dash"),
    html.P(
        children=(
            "Analyze the men's 200 meter times of the top ranked US athletes throughout the years in ascending order"
        ),
    ),
    dcc.Graph(
        figure={
            "data": [
                {
                    "x": data["name"],
                    "y": data["mark"],
                    "type": "lines",
                },
            ],
            "layout": {"title": "Average 200M times"}
        },
    ),
    dcc.Graph(
        figure={
            "data": [
                {
                    "x": data["name"],
                    "y": data["rank"],
                    "type": "plot",
                },
            ],
            "layout": {"title": "All Time Rank"},
        },
    ),
 ]

)

if __name__ == '__main__':
    app.run_server(debug=True)