#Import libraries
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import base64

from dash import Dash, dcc, html, Input, Output


data = (
    pd.read_csv('csv/100W.csv')
   
    .query("nat == 'USA'")
    .assign(Date=lambda data: pd.to_datetime(data["date"], format="%Y-%m-%d"))
    .sort_values(by="mark")
)

app = Dash(__name__, external_stylesheets=['/assets/css/w100dash.css'])


app.layout = html.Div(
    children=[
    html.H1(children="Women's 100 Dash all time"),
    html.P(
        children=(
            "Analyze the women's 100 meter times of the top ranked US athletes of all time."
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
                    "y": data["Date"],
                    "type": "plot",
                },
            ],
            "layout": {"title": "Date Ran"},
        },
    ),
 ]

)

if __name__ == '__main__':
    app.run_server(debug=True)