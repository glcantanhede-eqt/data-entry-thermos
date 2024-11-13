import streamlit as st
import pandas as pd
from st_supabase_connection import SupabaseConnection
import plotly.express as ex

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

### Help Funcs
def pick_color(value):
    # style = """<style>
    # div[data-testid='stMetric'] {{
    # border: 1px solid #c6c9fd;
    # padding: 10%% 10%% 10%% 10%%;
    # border-radius: 5px;
    # border-left: 0.5rem solid #1a008e !important;
    # box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;
    # }}

    # div.st-emotion-cache-1wivap2.e1i5pmia3 {{
    # color: {color_pick};
    # }}
    # </style>"""

    if value < 0.36:
        return "#eb4034" #style.format(color_pick="#eb4034")
    elif value < 0.71:
        return "#ffaa00" #style.format(color_pick="#ffaa00")
    else:
        return "#00b509" #style.format(color_pick="#00b509")


### Data Entry sanity check ###
df_user = None
if 'user_data' in st.session_state.keys():
    user_data = pd.DataFrame.from_dict(data=st.session_state['user_data'], orient='index').T
    dig_mentions = pd.DataFrame.from_dict(data=st.session_state['dig_mentions'], orient='index').T 
    press_mentions = pd.DataFrame.from_dict(data=st.session_state['press_mentions'], orient='index').T
    text_dig = st.session_state['text_dig']
    text_imp = st.session_state['text_imp']

    # Calculating the saudability and configuring the string format
    val_saud = dig_mentions[['dig_pos', 'dig_neu']].T.sum()/dig_mentions.T.sum()
    styled_val_dig = pick_color(val_saud[0])
    #st.markdown(styled_val_dig, unsafe_allow_html=True)
    #str_saud = f"<h1 style='color: {styled_val_dig};'>{val_saud[0]*100:.2f}</h1> %"

    # Calculating the favorability and configuring the string format
    val_fav = press_mentions['press_pos'].T.sum()/press_mentions.T.sum()
    styled_val_press = pick_color(val_fav[0])
    #st.markdown(styled_val_press, unsafe_allow_html=True)
    #str_fav = f"<h1 style='color: {styled_val_press};'>{val_fav[0]*100:.2f}</h1> %"

         

#conn = st.connection("supabase", type=SupabaseConnection)

try:
    user_fstring = f"""
    ## Dados do Usuário
    + **Matrícula**: {user_data['id_user'][0]} 
    + **Email**: {user_data['email'][0]}
    + **Empresa**: {user_data['business'][0]}
    + **Praça**: {user_data['place'][0]}
    """
    st.markdown(user_fstring)

    st.markdown("## Digital")
    col1, col2 = st.columns([0.4, 0.6], vertical_alignment='center')
    with col1:
        st.markdown("**Quantidade de Menções**")
        st.dataframe(dig_mentions, column_config={'dig_pos':'Positivas', 'dig_neu':'Neutras', 'dig_neg':'Negativas'}, hide_index=True)
    with col2:
        st.markdown("**Saudabilidade**")
        st.markdown(f"<h1 style='color:{styled_val_dig}'>{val_saud[0]*100:.2f} %</h1>",unsafe_allow_html=True)
    
    
    st.markdown("## Imprensa")
    col3, col4 = st.columns([0.4, 0.6], vertical_alignment='center')
    with col3:
        st.markdown("**Quantidade de Notícias**")
        st.dataframe(press_mentions, column_config={'press_pos':'Positivas', 'press_neg':'Negativas'}, hide_index=True)
    with col4:
        st.markdown("**Favorabilidade**")
        st.markdown(f"<h1 style='color:{styled_val_press}'>{val_fav[0]*100:.2f} %</h1>",unsafe_allow_html=True)



    check_ok = st.checkbox("Eu li os dados acima e confirmei que estão corretos.")
    if check_ok:
        button_submit = st.button("Enviar")
    

except:
    st.write("Erro ao recuperar dados do termômetro, preencha novamente os campos.")




#### Navigation buttons ###

st.markdown("-----")
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
with nav_prev:
    st.page_link("views/text_entry_page.py", label="Voltar")
#with nav_next:
#    st.page_link("views/text_entry_page.py", label="Avançar", disabled=True)