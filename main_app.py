import streamlit as st


# Background image to use -> https://energiaemdia.equatorialenergia.com.br/img/bg.webp
st.logo("https://www.equatorialenergia.com.br/wp-content/themes/equatorial-energia-child/img/logo-blue.png")

#st.set_page_config(page_title="Termômetro Reputacional", page_icon=":thermometer:", layout="wide", initial_sidebar_state="expanded") # makes the widgets expand to the full lenght of the screen almost
st.set_page_config(page_title="Termômetro Reputacional", page_icon=":thermometer:", layout="centered",) # initial_sidebar_state="collapsed")


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

ft = """
<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'> Gerência Corporativa de Comunicação Externa, Marketing e Sustentabilidade<br 'style= top:3px;'>
Feito com <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/> por <a href="mailto:gabriel.cantanhede@equatorialenergia.com.br"> Gabriel Cantanhede</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)

pg = st.navigation(pages, position='hidden')

pg.run()