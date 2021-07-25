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
st.text("Updated on " + max_date + " ,App by Argyrios Georgiadis, Source: https://ourworldindata.org/coronavirus")

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

new_tests = go.Figure()
new_tests.add_trace(go.Bar(x=greece['date'],
y=greece['new_tests'],
name='New Tests'))
new_tests.add_trace(go.Scatter(x=greece['date'],
y=greece['new_tests_smoothed'],
name='7 Days Rolling Average',
mode='lines'))
new_tests.update_layout({'title': {'text':
'Daily new tests',
'x': 0.3, 'y': 0.9}})
new_tests.update_layout(plot_bgcolor='rgb(255,255,255)',paper_bgcolor='rgb(250,250,250)')
new_tests.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgb(245,245,245)')
new_tests.update_xaxes(title_text='Day')
new_tests.update_yaxes(title_text='New Tests')
st.write(new_tests)

new_vaccinations = go.Figure()
new_vaccinations.add_trace(go.Bar(x=greece['date'],
y=greece['new_vaccinations'],
name='New Vaccinations'))
new_vaccinations.add_trace(go.Scatter(x=greece['date'],
y=greece['new_vaccinations_smoothed'],
name='7 Days Rolling Average',
mode='lines'))
new_vaccinations.update_layout({'title': {'text':
'Daily New Vaccinations',
'x': 0.3, 'y': 0.9}})
new_vaccinations.update_xaxes(range=["2021-01-01", max_date])
new_vaccinations.update_layout(plot_bgcolor='rgb(255,255,255)',paper_bgcolor='rgb(250,250,250)')
new_vaccinations.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgb(245,245,245)')
new_vaccinations.update_xaxes(title_text='Day')
new_vaccinations.update_yaxes(title_text='New Vaccinations')
st.write(new_vaccinations)


reproduction_rate = go.Figure()
reproduction_rate.add_trace(go.Scatter(x=greece["date"], y=greece["reproduction_rate"],
                    mode='lines+markers'))
reproduction_rate.update_layout({'title': {'text':
'Reproduction Rate of Covid-19',
'x': 0.3, 'y': 0.9}})
reproduction_rate.update_layout(plot_bgcolor='rgb(255,255,255)',paper_bgcolor='rgb(250,250,250)')
reproduction_rate.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgb(245,245,245)')
reproduction_rate.update_xaxes(range=["2020-03-01", max_date])

reproduction_rate.update_xaxes(title_text='Day')
reproduction_rate.update_yaxes(title_text="Reproduction Rate")
st.write(reproduction_rate)
