import streamlit as st
import numpy as np
import pandas as pd 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title('Greece Covid19 Live Data ')


#import data
path = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
covid = pd.read_csv(path)
greece = covid[covid.location == "Greece"]
max_date = max(greece.date)
st.text("Updated on " + max_date)

new_cases = go.Figure()
new_cases.add_trace(go.Bar(x=greece['date'],
y=greece['new_cases'],
name='New Cases'))
new_cases.add_trace(go.Scatter(x=greece['date'],
y=greece['new_cases_smoothed'],
name='7 Days Rolling Average',
mode='lines'))
new_cases.update_layout({'title': {'text':
'Daily new confirmed COVID-19 cases',
'x': 0.3, 'y': 0.9}})
new_cases.update_layout(plot_bgcolor='rgb(255,255,255)',paper_bgcolor='rgb(250,250,250)')
new_cases.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgb(245,245,245)')
new_cases.update_xaxes(title_text='Day')
new_cases.update_yaxes(title_text='New Cases')

st.write(new_cases)

new_deaths = go.Figure()
new_deaths.add_trace(go.Bar(x=greece['date'],
y=greece['new_deaths'],
name='New Deaths'))
new_deaths.add_trace(go.Scatter(x=greece['date'],
y=greece['new_deaths_smoothed'],
name='7 Days Rolling Average',
mode='lines'))
new_deaths.update_layout({'title': {'text':
'Daily new confirmed COVID-19 deaths',
'x': 0.3, 'y': 0.9}})
new_deaths.update_layout(plot_bgcolor='rgb(255,255,255)',paper_bgcolor='rgb(250,250,250)')
new_deaths.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgb(245,245,245)')
new_deaths.update_xaxes(title_text='Day')
new_deaths.update_yaxes(title_text='New Deaths')
st.write(new_deaths)
