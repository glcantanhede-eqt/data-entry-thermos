import streamlit as st
import control.db_connection as dbc
import time
from datetime import datetime, timezone

conn = None
if "__conn" not in st.session_state:
    conn = dbc.init_connection()
    st.session_state['__conn'] = conn
else:
    conn = st.session_state['__conn']

if "ts_start" not in st.session_state.keys():
    st.session_state["ts_start"] = str(datetime.now(tz=timezone.utc))

curr_user = conn.auth.get_session()
if curr_user:
    st.write(f"## Bem vindo(a), :blue[{curr_user.user.user_metadata["first_name"]}]!")
    with st.container(border=True):
        st.markdown("#### Prossiga para a próxima página ->")

else:
    #######
    st.markdown("##	:bust_in_silhouette: :blue[Login de Usuário]")

    with st.container(border=True):
        email_user = st.text_input("Email", placeholder="Insira seu email cadastrado", key="_email")
        pwd_user = st.text_input("Senha",type='password', key="_pwd")
        btn_login = st.button("Entrar")

        #saving the user data into the session state
        if btn_login:
            try:
                response = conn.auth.sign_in_with_password(dict(email=email_user, password=pwd_user))
                # st.session_state['__conn'] = conn
                time.sleep(2)
                st.write(f"## Bem vindo(a), :blue[{response.user.user_metadata["first_name"]}]!")
                
            except Exception as e:
                st.write("Erro ao tentar fazer login")
                e


#### Navigation buttons ###
# st.markdown("-----")
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
with nav_prev:
    st.page_link("views/landing_page.py", label="Voltar")
with nav_next:
    st.page_link("views/digital_mentions_page.py", label="Avançar",)
