import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
car_data = pd.read_csv("./vehicles_us.csv")


st.header(
    "Análisis Exploratorio de Datos (EDA) para el Dataset de Vehículos en Estados Unidos"
)
hist_button = st.button("Mostrar Histograma del Odómetro")
if hist_button:
    st.write(
        "En esta sección, realizaremos un análisis exploratorio de datos (EDA) para comprender mejor el dataset de vehículos en Estados Unidos. El EDA nos permitirá identificar patrones, tendencias y posibles relaciones entre las variables presentes en el dataset."
    )

    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"], nbinsx=50)])
    fig.update_layout(title="Distribución del odómetro")
    st.plotly_chart(fig)

scatter_button = st.button("Mostrar Gráfico de Dispersión entre Precio y Odómetro")
if scatter_button:
    st.write(
        "A continuación, exploraremos la relación entre el precio de los vehículos y su odómetro. Esto nos ayudará a entender si existe alguna correlación entre estas dos variables."
    )

    fig = px.scatter(
        car_data, x="odometer", y="price", title="Relación entre Precio y Odómetro"
    )
    st.plotly_chart(fig)
