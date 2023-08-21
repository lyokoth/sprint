import pandas as pd
import streamlit as st
import plotly.graph_objs as go
from plotly.subplots import make_subplots 
import os 

script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the CSV file
csv_file_path = os.path.join(script_dir, 'csv', '100M_Male.csv')

# Load data
data = pd.read_csv(csv_file_path)

# Create a Plotly figure
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=data['name'], y=data['mark'], name='Mark'),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=data['name'], y=data['wind'], name="Wind"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Men's Outdoor 100m Dash"
)

fig.update_xaxes(title_text="name")

fig.update_yaxes(title_text="<b>time</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>wind</b>", secondary_y=True)

# Streamlit App
st.title("Men's Outdoor 100 Meter Dash")
st.markdown(
    "Analyze the men's 100 meter times of the top ranked US athletes throughout the years in ascending order. "
   
)
st.markdown("Dark Blue = Wind, Light Blue = Time")

# Display the Plotly figure using the Plotly chart component
st.plotly_chart(fig)

