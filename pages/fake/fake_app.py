import streamlit as st
import src.fake_data_generator as fg
import pandas as pd
import io

def page_gerar_fake():
    st.title('Gerador de Dados Fícticios')

    #Selecionando o formato do arquivo
    formato = st.selectbox('Formato', ['.csv', '.txt'])

    #Selecionando a quantidade de dados que serão gerados
    quantidade_linhas = st.number_input('Quantidade de Linhas', step=1, min_value=0, max_value=2000)

    #Selecionando os tipos de dados
    lista_campos = [campo for campo in fg.dict_opcoes().keys()]
    campos = st.multiselect('Campos', lista_campos)

    botao_download = st.button('Download de Dados')

    if botao_download and campos and quantidade_linhas:
        with st.spinner('Aguarde enquanto é gerado os dados...'):
            arquivo_csv = fg.gerar_csv_memoria(quantidade_linhas, campos)
        st.success("Dados gerados com sucesso")
        st.dataframe(arquivo_csv)
    elif botao_download and (not campos or not quantidade_linhas):
        st.warning('Selecione pelo menos uma linha e ao menos um campo!', icon="⚠️")