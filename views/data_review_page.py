import streamlit as st
import pandas as pd
from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions
import json

@st.cache_resource
def init_connection():
    opts = ClientOptions().replace(schema="data_entry")
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key, options=opts)

with st.spinner("Processando dados..."):
# Intializing connection
    supabase = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_resource(ttl=600)
def run_select(_table_name, atributes):
    return supabase.table(_table_name).select(atributes).execute()


@st.cache_resource(ttl=600)
def run_insert(_table_name, values):
    return supabase.table(_table_name).insert(values).execute()


#### Importing custom styling into the page 

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

### Help Funcs
def pick_color(value):
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
    text_press = st.session_state['text_press']

    # Calculating the saudability and configuring the string format
    val_saud = (dig_mentions[['dig_pos', 'dig_neu']].T.sum()/dig_mentions.T.sum())*100
    styled_val_dig = pick_color(val_saud[0])


    # Calculating the favorability and configuring the string format
    val_fav = (press_mentions['press_pos'].T.sum()/press_mentions.T.sum())*100
    styled_val_press = pick_color(val_fav[0])
    val_overall = ((val_saud + val_fav) / 2 )
    styled_val_overall = pick_color(val_overall[0])

    # Preparing the dict to be inserted
    dict_insert = dict(
                id_user = user_data['id_user'][0],
                email = user_data['email'][0],
                business = user_data['business'][0],
                place = user_data['place'][0],
                press_pos = int(press_mentions['press_pos'][0]), 
                press_neg = int(press_mentions['press_neg'][0]), 
                dig_pos = int(dig_mentions['dig_pos'][0]), 
                dig_neu = int(dig_mentions['dig_neu'][0]), 
                dig_neg = int(dig_mentions['dig_neg'][0]), 
                text_press = str(text_press), 
                text_dig = str(text_dig),
                favorability = val_fav[0], 
                saudability = val_saud[0], 
                overall_fav = val_overall[0])
         

#conn = st.connection("supabase", type=SupabaseConnection)

try:
    user_fstring = f"""
    ## :bust_in_silhouette: Dados do Usuário
    + **Matrícula**: {user_data['id_user'][0]} 
    + **Email**: {user_data['email'][0]}
    + **Empresa**: {user_data['business'][0]}
    + **Praça**: {user_data['place'][0]}
    """
    st.markdown(user_fstring)

    st.markdown("## :iphone: Digital")
    col1, col2 = st.columns([0.4, 0.6], vertical_alignment='center')
    with col1:
        st.markdown("**Quantidade de Menções**")
        st.dataframe(dig_mentions, column_config={'dig_pos':'Positivas', 'dig_neu':'Neutras', 'dig_neg':'Negativas'}, hide_index=True)
    with col2:
        st.markdown("**Saudabilidade**")
        st.markdown(f"<h1 style='color:{styled_val_dig}'>{val_saud[0]:.2f} %</h1>",unsafe_allow_html=True)
    
    
    st.markdown("## :newspaper: Imprensa")
    col3, col4 = st.columns([0.4, 0.6], vertical_alignment='center')
    with col3:
        st.markdown("**Quantidade de Notícias**")
        st.dataframe(press_mentions, column_config={'press_pos':'Positivas', 'press_neg':'Negativas'}, hide_index=True)
    with col4:
        st.markdown("**Favorabilidade**")
        st.markdown(f"<h1 style='color:{styled_val_press}'>{val_fav[0]:.2f} %</h1>",unsafe_allow_html=True)

    col5, col6 = st.columns([0.4, 0.6], vertical_alignment='center')
    with col5:
        st.markdown("## :thermometer: Como estamos hoje?")
    with col6:
        st.markdown(f"<h1 style='color:{styled_val_overall}'>{val_overall[0]:.2f} %</h1>",unsafe_allow_html=True)
    

    check_ok = st.checkbox("Eu li os dados acima e confirmei que estão corretos.")
    if check_ok:
        button_submit = st.button("Enviar")
        # connecting to supabase and inserting data
        if button_submit:

            # insert_query = f"""
            # INSERT INTO data_entry.raw_data (id_user, email, business, place, press_pos, press_neg, dig_pos, dig_neu, dig_neg, text_press, text_dig, favorability, saudability, overall_fav)
            # VALUES
            # ({user_data['id_user'][0]}, {user_data['email'][0]}, {user_data['business'][0]}, {user_data['place'][0]}, {press_mentions['press_pos']}, {press_mentions['press_neg']}, {dig_mentions['dig_pos']}, {dig_mentions['dig_neu']}, {dig_mentions['dig_neg']}, {text_press}, {text_dig}, {val_fav}, {val_saud}, {val_overall})
            # """
            # rows = run_insert('raw_data', dict_insert)
            with st.spinner("Processando dados..."):
                rows = run_select("raw_data", "*")
            if rows:
                st.write("Sucesso!")

except Exception as ex:
    st.write("Erro ao recuperar dados, preencha novamente os campos.")
    st.write(ex)




#### Navigation buttons ###

st.markdown("-----")
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
with nav_prev:
    st.page_link("views/text_entry_page.py", label="Voltar")
#with nav_next:
#    st.page_link("views/text_entry_page.py", label="Avançar", disabled=True)