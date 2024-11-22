import streamlit as st
import pandas as pd
# from supabase import create_client, Client
# from supabase.lib.client_options import ClientOptions
import control.db_connection as dbc
import json

conn = None
if "__conn" not in st.session_state:
    conn = dbc.init_connection()
    st.session_state['__conn'] = conn
else:
    conn = st.session_state['__conn']

# @st.cache_resource
# def init_connection():
#     opts = ClientOptions().replace(schema="data_entry")
#     url = st.secrets["SUPABASE_URL"]
#     key = st.secrets["SUPABASE_KEY"]
#     return create_client(url, key, options=opts)

# with st.spinner("Processando dados..."):
# # Intializing connection
#     conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_resource(ttl=600)
# def run_select(conn,_table_name, atributes):
#     return conn.table(_table_name).select(atributes).execute()


# @st.cache_resource(ttl=600)
# def run_insert(_table_name, values):
#     return conn.table(_table_name).insert(values).execute()


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
curr_user = conn.auth.get_user()
user_data = None
if curr_user:
    user_data = curr_user.user.user_metadata
    user_data


if 'text_warn' in st.session_state.keys():
    # Transforming and storing the data in adequate variables
    # user_data = pd.DataFrame.from_dict(data=st.session_state['user_data'], orient='index').T
    dig_mentions = pd.DataFrame.from_dict(data=st.session_state['dig_mentions'], orient='index').T 
    press_mentions = pd.DataFrame.from_dict(data=st.session_state['press_mentions'], orient='index').T
    text_pos = st.session_state['text_pos']
    text_warn = st.session_state['text_warn']

    # Calculating the saudability and configuring the string format
    val_saud = (dig_mentions[['dig_pos', 'dig_neu']].T.sum()/dig_mentions.T.sum())*100
    styled_val_dig = pick_color(val_saud[0])

    # Calculating the favorability and configuring the string format
    val_fav = (press_mentions['press_pos'].T.sum()/press_mentions.T.sum())*100
    styled_val_press = pick_color(val_fav[0])

    # Calculating the overall favorability for the brand
    val_overall = ((val_saud + val_fav) / 2 )
    styled_val_overall = pick_color(val_overall[0])

    # Preparing the dict to be inserted
    dict_insert = dict(
                id_user = user_data['id_user'],
                email = user_data['email'],
                business = user_data['business'],
                place = user_data['place'],
                press_pos = int(press_mentions['press_pos'][0]), 
                press_neg = int(press_mentions['press_neg'][0]), 
                dig_pos = int(dig_mentions['dig_pos'][0]), 
                dig_neu = int(dig_mentions['dig_neu'][0]), 
                dig_neg = int(dig_mentions['dig_neg'][0]), 
                text_pos = str(text_pos), 
                text_warn = str(text_warn),
                favorability = val_fav[0], 
                saudability = val_saud[0], 
                overall_fav = val_overall[0])
         

#conn = st.connection("supabase", type=SupabaseConnection)

try:
    with st.container(border=True):
        user_fstring = f"""
        ## :bust_in_silhouette: Dados do Usuário
        + **Matrícula**: {user_data['id_user']} 
        + **Email**: {user_data['email']}
        + **Empresa**: {user_data['business']}
        + **Praça**: {user_data['place']}
        """
        st.markdown(user_fstring)

        st.markdown("## :iphone: Digital")
        col1, col2 = st.columns([0.7, 0.3], vertical_alignment='center')
        with col1:
            st.markdown("**Quantidade de Menções**")
            st.dataframe(dig_mentions, column_config={'dig_pos':'Positivas', 'dig_neu':'Neutras', 'dig_neg':'Negativas'}, hide_index=True)
        with col2:
            st.markdown("**Saudabilidade**")
            st.markdown(f"<h1 style='color:{styled_val_dig}'>{val_saud[0]:.2f} %</h1>",unsafe_allow_html=True)
        
        st.markdown(f":green-background[Pontos Positivos: {text_pos['dig']}]")
        st.markdown(f":orange-background[Pontos de Atenção: {text_warn['dig']}]")
        
        st.markdown("## :newspaper: Imprensa")
        col3, col4 = st.columns([0.7, 0.3], vertical_alignment='center')
        with col3:
            st.markdown("**Quantidade de Notícias**")
            st.dataframe(press_mentions, column_config={'press_pos':'Positivas', 'press_neg':'Negativas'}, hide_index=True)
        with col4:
            st.markdown("**Favorabilidade**")
            st.markdown(f"<h1 style='color:{styled_val_press}'>{val_fav[0]:.2f} %</h1>",unsafe_allow_html=True)

        st.markdown(f":green-background[Pontos Positivos: {text_pos['press']}]")
        st.markdown(f":orange-background[Pontos de Atenção: {text_warn['press']}]")

        col5, col6 = st.columns([0.7, 0.3], vertical_alignment='center')
        with col5:
            st.markdown("## :thermometer: Como estamos hoje?")
        with col6:
            st.markdown(f"<h1 style='color:{styled_val_overall}'>{val_overall[0]:.2f} %</h1>",unsafe_allow_html=True)
        

    check_ok = st.checkbox("Eu li os dados acima e confirmei que estão corretos.")
    if check_ok:
        button_submit = st.button("Enviar")
        # connecting to supabase and inserting data if the button is pressed
        if button_submit:
            rows = run_insert('raw_data', dict_insert)
            if rows.data:
                st.success("Dados enviados com sucesso!")

except Exception as ex:
    st.write("Erro ao processar dados, tente novamente.")
    st.write(ex) # OG debugging




#### Navigation buttons ###
# st.markdown("-----")
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
with nav_prev:
    st.page_link("views/text_entry_page.py", label="Voltar")
#with nav_next:
#    st.page_link("views/text_entry_page.py", label="Avançar", disabled=True)