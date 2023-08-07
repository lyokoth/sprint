import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from plotly.subplots import make_subplots 


data = pd.read_csv('csv/100M_Male.csv')

app = dash.Dash(__name__, external_stylesheets=['/assets/css/m100.css'])

app.layout = html.Div([
    html.H1(children="Men's Outdoor 100 Meter Dash", style={'backgroundColor': 'black'}),
    html.P(
        children="Analyze the men's 100 meter times of the top ranked US athletes throughout the years in ascending order",
    ),

    dcc.Graph(id='scatter-plot'),

])

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=(data['name']), y=(data['mark']), name='Mark'),
    secondary_y = False,
)


fig.add_trace(
    go.Scatter(x=(data['name']), y=(data['wind']), name="Time"),
    secondary_y = True,
)

fig.update_layout(
    title_text = "Men's Outdoor 100m Dash"
)

fig.update_xaxes(title_text="name")

fig.update_yaxes(title_text="<b>time</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>wind</b>", secondary_y=True)

fig.show()

if __name__ == '__main__':
    app.run_server(debug=True)
