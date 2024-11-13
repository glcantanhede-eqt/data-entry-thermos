import streamlit as st
import time
from control.misc_funcs import showProgressBar

## Data Entry Class ##
from model.data_entry import Data_Entry



#TODO show datetime timestamp on screen, or allow for user to pick a date
st.markdown("##	:bust_in_silhouette: :blue[Dados do Usuário]")

## Session Initialization and variable handling
# Get the User Data from the session, in case the user changes pages
if 'user_data' in st.session_state.keys():
    curr_id = st.session_state['user_data']['id_user']
    curr_email = st.session_state['user_data']['email']
    curr_business = st.session_state['user_data']['business']
    curr_place = st.session_state['user_data']['place']
else:
    curr_id = 10000
    curr_email = None
    curr_business = None
    curr_place = None

#######

id_user = st.number_input("Insira sua matrícula (apenas números)", value = curr_id, format="%i", key='_id_user')

email_user = st.text_input("Insira seu email institucional", value = curr_email, key='_email')
# regex_email = r"^\S+@\S+$"


#TODO include user email var, with email validation. 

col1, col2 = st.columns(2)
with col1:
    opt_business = st.selectbox(
        "Selecione sua Empresa:",
        ("Distribuição", "Saneamento", "Serviços", "Eólica", "Solar"),
        index=None,
        placeholder="Selecione uma opção",
        key='_business'
    )
    st.markdown(f"Empresa selecionada: :green[{st.session_state['_business']}]")
    
with col2:
    opt_place = st.selectbox(
        "Selecione sua Praça:",
        ("AL", "AP", "GO", "MA", "PA", "PI", "RS"),
        index=None,
        placeholder="Selecione uma opção",
        key='_place'
        )
    st.markdown(f"Praça selecionada: :green[{st.session_state['_place']}]")



mask_show_button = not(id_user and email_user and opt_business and opt_place)

save_user_button = st.button("Salvar", disabled=mask_show_button)

#saving the user data into the session state
if save_user_button:
    st.session_state['user_data'] = {
        'id_user': st.session_state['_id_user'],
        'email': st.session_state['_email'],
        'business': st.session_state['_business'],
        'place': st.session_state['_place']
    }

#####
st.markdown("-----")

#### Navigation buttons ###
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
with nav_prev:
    st.page_link("views/landing_page.py", label="Voltar")
with nav_next:
    st.page_link("views/digital_mentions_page.py", label="Avançar",)
