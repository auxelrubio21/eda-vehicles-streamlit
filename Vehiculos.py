import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Dashboard de autos usados')

data = pd.read_csv('vehicles_us.csv')

if st.button('Mostrar histograma'):
    fig = px.histogram(data, x='odometer')
    st.plotly_chart(fig)

if st.button('Mostrar dispersión'):
    fig = px.scatter(data, x='model_year', y='price', color='type')
    st.plotly_chart(fig)
