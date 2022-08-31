from calendar import c

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from st_aggrid import AgGrid

df = pd.read_csv('./topMovies.csv', sep=',')

# menu lateral
st.sidebar.title('Menu')
pagina_selecionada = st.sidebar.selectbox(
    'Selecionar página', ['Home', 'Dados', 'Gráficos'])

# mostrar homepage
if pagina_selecionada == 'Home':
    st.title('Análise de dados - Top 200 Filmes IMDB')
    link = 'https://www.kaggle.com/datasets/ayushv322/top-200-movies-imdb'
    st.write(f'fonte: {link}')

# mostrar tabela
if pagina_selecionada == 'Dados':
    st.title('Dados')

    # tabela com opçãoes de filtrar
    AgGrid(df)

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='#000036', align='center'),
        cells=dict(
            values=[df.Title, df.Year_of_Release, df.Rating, df.Number_of_Reviews, df.Popularity_Index, df.Movie_Cast,
                    df.Director, df.Description],
            fill_color='#001648', align='center'))
    ])
    st.write(fig)

# mostrar gráficos
if pagina_selecionada == 'Gráficos':
    st.title('Gráficos')
    col1, col2 = st.columns(2)

# tabela agrupada pelos interesses

    df_01 = df.groupby(['Year_of_Release', 'Rating',
                       'Director']).size().reset_index()
# gráficos 1 e 2:
    fig_01 = px.histogram(df_01, color='Director', x='Year_of_Release')
    st.plotly_chart(fig_01)

    fig_02 = px.histogram(df_01, color='Rating', x='Year_of_Release')
    st.plotly_chart(fig_02)
