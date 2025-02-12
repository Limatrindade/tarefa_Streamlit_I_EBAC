import streamlit as st  # type: ignore
import pandas as pd
import numpy as np
import os

st.title('Análise de Dados de Vacinação')

# Caminho do arquivo de dados
DATA_URL = 'c:/Users/alima/OneDrive/Documentos/ebac/Streamlit - EBAC - I/dados_vacina.csv'

# Verifica se o arquivo existe antes de tentar carregá-lo
if os.path.exists(DATA_URL):
    @st.cache_data
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, sep=';', nrows=nrows)
        return data

    data_load_state = st.text('Carregando os dados...')
    data = load_data(10000)
    data_load_state.text("Dados carregados com sucesso!")

    if st.checkbox('Mostrar dados brutos'):
        st.subheader('Dados brutos')
        st.write(data)

    st.subheader('Distribuição das Vacinas Aplicadas')
    if 'vacina_nome' in data.columns:
        vacina_counts = data['vacina_nome'].value_counts()
        st.bar_chart(vacina_counts)
    else:
        st.error("A coluna 'vacina_nome' não foi encontrada nos dados.")

    # Verifica as colunas disponíveis no DataFrame
    st.write("Colunas disponíveis nos dados:", data.columns)

else:
    st.error("Arquivo de dados não encontrado. Por favor, carregue o arquivo 'dados_vacina.csv'.")


