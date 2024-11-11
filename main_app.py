import streamlit as st
# Imagem bg pra usar -> https://energiaemdia.equatorialenergia.com.br/img/bg.webp
#with st.sidebar:
# st.logo("https://energiaemdia.equatorialenergia.com.br/img/logo-equatorial.png")
st.logo("https://www.equatorialenergia.com.br/wp-content/themes/equatorial-energia-child/img/logo-blue.png")
#st.set_page_config(page_title="Termômetro Reputacional", page_icon=":thermometer:", layout="wide", initial_sidebar_state="expanded") # makes the widgets expand to the full lenght of the screen almost
st.set_page_config(page_title="Termômetro Reputacional", page_icon=":thermometer:", layout="centered", initial_sidebar_state="collapsed")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

pages = {
    "Início":[
        st.Page("./views/landing_page.py", title="Instruções", default=True, icon='📖'),
        st.Page("./views/user_data_page.py", title="Dados do Usuário", icon='👤'),
        ],
    "Dados do Termômetro": [
        st.Page("./views/digital_mentions_page.py", title="Digital", icon='📱'),
        st.Page("./views/press_mentions_page.py", title="Imprensa", icon='📰'),
        st.Page("./views/text_entry_page.py", title="Observações", icon='📝')
        ],
    "Final": [
        st.Page("./views/data_review_page.py", title="Revisão dos Dados", icon='✔️'),
        ]
    
    }

pg = st.navigation(pages)

pg.run()