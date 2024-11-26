import streamlit as st
from datetime import datetime, timezone


if "ts_landing" not in st.session_state.keys():
    st.session_state["ts_landing"] = str(datetime.now(tz=timezone.utc))
    

st.markdown("# :thermometer: :blue[Bem vindo ao Termômetro Reputacional do Grupo Equatorial]")

with st.container(border=True):
    st.markdown("""Insira os dados em seus respectivos campos, conforme o fluxo deste formulário.
    **Tenha atenção extra ao inserir os dados numéricos,**,
    do contrário os cálculos do termômetro serão afetados. """)

#### Navigation buttons ###
# st.markdown("-----")
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
#with nav_prev:
#    st.page_link("views/data_review_page.py", label="Voltar", disabled=True)
with nav_next:
    st.page_link("views/user_login.py", label="Avançar",)