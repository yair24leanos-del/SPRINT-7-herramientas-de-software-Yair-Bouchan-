# importamos librerias
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# se lee la data
car_data = pd.read_csv(
    r"/mnt/c/Users/YairE/Desktop/ACAB/Proyectos/DataScience/Proyectos/Proyecto_sprint_7/SPRINT-7-herramientas-de-software-Yair-Bouchan--1/vehicles_us.csv")

# agregamos titulo
st.header('Car Data')

# agregamos el boton 1: price/Odometer
hist_button1 = st.button('mostrar histograma odometer')

# logica del boton, crea mensaje e histograma
if hist_button1:

    # crea mensaje
    st.write('Creado histograma para odometer')

    # crea histograma con plotly, primero figura vacia y despues se a;ade el rastro del histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # crea titulo para el histograma
    fig.update_layout(title_text='distribucion del odometer')

    # muestra el histograma en streamlit
    st.plotly_chart(fig, use_container_width=True)

# agregamos el boton 2: price/type
hist_button2 = st.button('mostrar histograma price/type')

# logica del boton, crea mensaje y grafico de dispersion
if hist_button2:

    # crea mensaje:
    st.write('Creado grafico de dispersion para price/type')

    # crea grafico de dispersion con plotly, primero una figura vacia y despues se a;ade el rastro del grafico de dispersion
    fig = go.Figure(data=[go.Scatter(x=car_data['price'],
                    y=car_data['type'], mode='markers')])

    # crea un titulo para este grafico de dispersion
    fig.update_layout(title_text='distribucion del price/type')

    # muestra el grafico de dispersion en streamlit
    st.plotly_chart(fig, use_container_width=True)
