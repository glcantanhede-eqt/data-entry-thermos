import streamlit as st
import pandas as pd
import control.db_connection as dbc
import control.misc_funcs as misc
import time

ts_start = None
if 'ts_start' in st.session_state.keys():
    ts_start = st.session_state.ts_start
elif 'ts_landing' in st.session_state.keys():
    ts_start = st.session_state.ts_landing

conn = None
if "__conn" not in st.session_state:
    conn = dbc.init_connection()
    st.session_state['__conn'] = conn
else:
    conn = st.session_state['__conn']


#### Importing custom styling into the page 

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


### Fetching metadata from the logged user
curr_user = None
user_data = None
try:
    curr_user = conn.auth.get_session()
    user_data = curr_user.user.user_metadata
except:
    st.write("Erro ao recuperar dados do usuário, tente logar novamente.")

### Handling the thermometer data 
if 'text_warn' in st.session_state.keys():
    # Transforming and storing the data in adequate variables
    dig_mentions = pd.DataFrame.from_dict(data=st.session_state['dig_mentions'], orient='index').T 
    press_mentions = pd.DataFrame.from_dict(data=st.session_state['press_mentions'], orient='index').T
    text_pos = st.session_state['text_pos']
    text_warn = st.session_state['text_warn']

    # Calculating the saudability and configuring the string format
    val_saud = (dig_mentions[['dig_pos', 'dig_neu']].T.sum()/dig_mentions.T.sum())*100
    styled_val_dig = misc.pick_color(val_saud[0])

    # Calculating the favorability and configuring the string format
    val_fav = (press_mentions['press_pos'].T.sum()/press_mentions.T.sum())*100
    styled_val_press = misc.pick_color(val_fav[0])

    # Calculating the overall favorability for the brand
    val_overall = ((val_saud + val_fav) / 2 )
    styled_val_overall = misc.pick_color(val_overall[0])

    # Preparing the dict to be inserted
    dict_insert = dict(
                uuid = curr_user.user.id,
                worker_id = user_data['id_user'],
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
                overall_fav = val_overall[0],
                started_at = ts_start
                )
         

try:
    with st.container(border=True):
        with st.container(border=True):
            user_fstring = f"""
            ## :bust_in_silhouette: Dados do Usuário
            + **Matrícula**: {user_data['id_user']} 
            + **Email**: {user_data['email']}
            + **Empresa**: {user_data['business']}
            + **Praça**: {user_data['place']}
            """
            st.markdown(user_fstring)
        with st.container(border=True):
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
        
        with st.container(border=True):    
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
        with st.container(border=True):
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
            rows = dbc.run_insert(conn,'raw_data', dict_insert)
            st.success("Dados enviados com sucesso! Você já pode fechar esta página.")
            time.sleep(1)
            # conn.auth.sign_out()
    

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