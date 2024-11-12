import streamlit as st
import pandas as pd
from st_supabase_connection import SupabaseConnection
import plotly.express as ex

### Data Entry sanity check ###
df_user = None
if 'user_data' in st.session_state.keys():
    user_data = pd.DataFrame.from_dict(data=st.session_state['user_data'], orient='index').T
    dig_mentions = pd.DataFrame.from_dict(data=st.session_state['dig_mentions'], orient='index').T
    val_saud = dig_mentions['dig_pos']/dig_mentions.T.sum()
    press_mentions = pd.DataFrame.from_dict(data=st.session_state['press_mentions'], orient='index').T
    text_dig = st.session_state['text_dig']
    text_imp = st.session_state['text_imp']
#conn = st.connection("supabase", type=SupabaseConnection)

try:
    with st.form('data_form'):
        user_fstring = f"""
        #### Dados do Usuário
        + **Matrícula**: {user_data['id_user'][0]} 
        + **Email**: {user_data['email'][0]}
        + **Empresa**: {user_data['business'][0]}
        + **Praça**: {user_data['place'][0]}
        """
        st.markdown(user_fstring)

        st.markdown("#### Saudabilidade")
        col1, col2 = st.columns([0.4, 0.6], vertical_alignment='center')
        with col1:
            st.dataframe(dig_mentions, column_config={'dig_pos':'Positivas', 'dig_neu':'Neutras', 'dig_neg':'Negativas'}, hide_index=True)
        with col2:

            st.metric(label='SAUD', value=65, delta=-15, label_visibility='collapsed')
        st.markdown("#### Favorabilidade")
        st.dataframe(press_mentions, column_config={'press_pos':'Positivas', 'press_neg':'Negativas'}, hide_index=True)



        check_ok = st.checkbox("Eu li os dados acima e confirmei que estão corretos.")
        button_submit = st.form_submit_button("Enviar")
        

except:
    st.write("Erro ao recuperar dados do termômetro, preencha novamente os campos.")




#### Navigation buttons ###

st.markdown("-----")
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
with nav_prev:
    st.page_link("views/text_entry_page.py", label="Voltar")
#with nav_next:
#    st.page_link("views/text_entry_page.py", label="Avançar", disabled=True)