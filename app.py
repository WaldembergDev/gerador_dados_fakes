import streamlit as st
import pages.fake.fake_app as page_fg


st.sidebar.title('Menu')

pages_app = st.sidebar.selectbox('Opções', ['Gerador'])

if pages_app == 'Gerador':
    page_fg.page_gerar_fake()
        




    

