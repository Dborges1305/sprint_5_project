import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.header('Anúncios de Vendas de Carros')
st.write('Ainda não é um aplicativo funcional. Em construção.')

hist_button = st.button('Criar Histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig=px.histogram(car_data, x="type", y="price")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar Gráfico de Dispersão')
if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig=px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)

show_manufacturer = st.checkbox('Mostrar gráfico de fabricantes')
show_type = st.checkbox('Mostrar gráfico de tipos de carro')

car_data['manufacturer'] = car_data['model'].str.split().str[0]
manufacturer_counts = car_data['manufacturer'].value_counts().reset_index()

type_counts = car_data['type'].value_counts().reset_index()


if show_manufacturer:
    st.write('Gráfico de fabricantes para o conjunto de dados de anúncios de vendas de carros')
    fig = px.bar(manufacturer_counts, x='manufacturer', y='count', title='Número de carros por fabricante')
    st.plotly_chart(fig, use_container_width=True)

if show_type:
    st.write('Gráfico de tipos de carro para o conjunto de dados de anúncios de vendas de carros')
    fig = px.bar(type_counts, x='type', y='count', title='Número de carros por tipo')
    st.plotly_chart(fig, use_container_width=True)
