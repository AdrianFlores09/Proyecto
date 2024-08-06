import pandas as pd
import plotly.express as px
import streamlit as st
st.header("Odómetros de los vehículos en venta")        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Construir un Histograma')
build_dispersion = st.checkbox("Construir un Diagrama de Dispersión")

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer", title="Conteo de odómetros con su respectivo recorrido")
    st.plotly_chart(fig, use_container_width=True)
    
if build_dispersion: # si la casilla de verificación está seleccionada
    st.write('Construir un diagrama de dispersión para la columna odómetro')
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio de odómetros con su respectivo recorrido")
    fig.show()