import streamlit as st
# from supabase import create_client, Client
import control.db_connection as dbc 
import json

# # Initialize connection.
# @st.cache_resource
# def init_connection():
#     opts = ClientOptions().replace(schema="data_entry")
#     url = st.secrets["SUPABASE_URL"]
#     key = st.secrets["SUPABASE_KEY"]
#     return create_client(url, key, options=opts)

conn = dbc.init_connection()

st.markdown("# Cadastro de Usuário")
with st.container(border=True):
    id_user = st.number_input("Insira sua matrícula (apenas números)", value = 00000, format="%i", key='_id_user_signup')
    first_name = st.text_input("Insira seu primeiro nome", key='_name_signup')
    email_user = st.text_input("Insira seu email institucional", placeholder="email@empresa.com.br", key='_email_signup')
    pwd_user = st.text_input("Insira uma senha para acesso ao Termômetro", key= '_pwd', type='password')
    
    col1, col2 = st.columns(2)
    with col1:
        opt_business = st.selectbox(
            "Selecione sua Empresa:",
            ("Distribuição", "Saneamento", "Serviços", "Eólica", "Solar"),
            index=None,
            placeholder="Selecione uma opção",
            key='_business'
        )
        
    with col2:
        opt_place = st.selectbox(
            "Selecione sua Praça:",
            ("AL", "AP", "GO", "MA", "PA", "PI", "RS", "SP"),
            index=None,
            placeholder="Selecione uma opção",
            key='_place'
            )

dict_user = dict(
    email= email_user,
    password = pwd_user,
    options = dict(data = dict(
        id_user = id_user,
        first_name = first_name,
        business = opt_business,
        place = opt_place,
    )))

btn_signup = st.button("Cadastrar")

if btn_signup:
    try:
        response = conn.auth.sign_up(dict_user)
        if response.user:
            st.success("Usuário cadastrado com sucesso. Você receberá um email para confirmar seu cadastro.")
    except Exception as e:
        st.write("Problema ao cadastrar usuário")
        e
