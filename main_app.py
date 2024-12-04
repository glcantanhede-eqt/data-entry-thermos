import streamlit as st
# Imagem bg pra usar -> https://energiaemdia.equatorialenergia.com.br/img/bg.webp
st.logo("https://www.equatorialenergia.com.br/wp-content/themes/equatorial-energia-child/img/logo-blue.png")

#st.set_page_config(page_title="Termômetro Reputacional", page_icon=":thermometer:", layout="wide", initial_sidebar_state="expanded") # makes the widgets expand to the full lenght of the screen almost
st.set_page_config(page_title="Termômetro Reputacional", page_icon=":thermometer:", layout="centered", initial_sidebar_state="collapsed")

### Disabling the streamlit menu on production
styles = {
        "nav": {
            "background-color": "white",
            "display": "flex",
            
            "height": ".01rem"
        },
    }
options = {
    'show_menu': False
}#####

### Customizing the CSS, old style
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

### Setting up the pages
pages = {
    "Início":[
        st.Page("./views/landing_page.py", title="Instruções", default=True, icon='📖'),
        st.Page("./views/user_login.py", title="Login de Usuário", icon='👤'),
        # st.Page("./views/user_create.py", title="Cadastrar Usuário", icon='👤'),
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

### Setting up the app navigation 
pg = st.navigation(pages, styles=styles, options=options)

pg.run()