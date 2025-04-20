import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

st.header('Explorador de Datos - Vehículos en Venta en EE.UU.')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar dataset si el usuario quiere
if st.checkbox("Mostrar datos"):
    st.write(car_data.head())

# Histograma
if st.button('Mostrar histograma (odómetro)'):
    st.plotly_chart(px.histogram(car_data, x='odometer',
                    title="Kilometraje"), use_container_width=True)

# Dispersión
if st.button('Mostrar dispersión (odómetro vs precio)'):
    st.plotly_chart(px.scatter(car_data, x='odometer', y='price',
                    title="Odómetro vs Precio"), use_container_width=True)
