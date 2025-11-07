import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado 
st.header("Analisis de Vehiculos Usados en EE.UU.")

# Conjunto de datos
df = pd.read_csv("../vehicles_us.csv")

# Vista previa
st.write("Vista previa del conjunto de datos:")
st.dataframe(df.head())

# Boton Histograma
if st.button("Mostrar histograma de precios"):
    st.write("Histograma de distribucion de precios")
    fig_hist = px.histogram(df, x="price", nbins=50, title="Distribucion de precios de vehiculos")
    st.plotly_chart(fig_hist)

# Boton Grafico de dispersion
if st.button("Mostrar grafico de dispersion precio vs año"):
    st.write("Grafico de dispersion: Precio vs Año del modelo")
    fig_scatter = px.scatter(df, x="model_year", y="price", color="condition", title="Precio vs Año del modelo")
    st.plotly_chart(fig_scatter)
