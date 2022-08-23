import pandas as pd
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv('./topMovies.csv', sep=',')

#menu lateral
st.sidebar.title('Menu')
pagina_selecionada = st.sidebar.selectbox(
    'Selecionar página', ['Home','Tabela', 'Gráficos'])

#mostrar homepage
if pagina_selecionada == 'Home':
    st.title('Análise de dados - Top 200 Filmes IMDB')
    st.write('fonte:')
    st.write('https://www.kaggle.com/datasets/ayushv322/top-200-movies-imdb')

#mostrar tabela
if pagina_selecionada == 'Tabela':
    st.title('Tabela')
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns), fill_color='#000036', align='center'),
        cells=dict(
            values=[df.Title, df.Year_of_Release, df.Rating, df.Number_of_Reviews, df.Popularity_Index, df.Movie_Cast,
                    df.Director, df.Description],
            fill_color='#001648', align='center'))
    ])
    st.write(fig)

#mostrar gráficos
if pagina_selecionada == 'Gráficos':
    st.title('Gráficos')
    df_01 = df.groupby(['Year_of_Release', 'Rating', 'Director', 'Number_of_Reviews']).size().reset_index()
    fig_01 = px.histogram(df_01, color = 'Rating', x ='Director')
    st.write(fig_01)
    fig_02 = px.histogram(df_01, color = 'Rating', x ='Year_of_Release')
    st.plotly_chart(fig_02)
