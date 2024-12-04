import streamlit as st

st.markdown("## :iphone: :blue[Termômetro Digital]")

# Initializing the session state
if 'dig_mentions' in st.session_state:
    curr_dig_positive = st.session_state['dig_mentions']['dig_pos']
    curr_dig_neutral = st.session_state['dig_mentions']['dig_neu']
    curr_dig_negative = st.session_state['dig_mentions']['dig_neg']
else:
    curr_dig_positive = 0
    curr_dig_neutral = 0
    curr_dig_negative = 0

with st.container(border=True):
    # Data entry part for Digital media
    col1, col2, col3 = st.columns(3)
    #Positive mentions
    with col1:
        dig_positive = st.number_input("Quantidade de **:green-background[Menções Positivas]**", value=curr_dig_positive, format="%d", key='_dig_pos')
        st.write("Positivas:", dig_positive)

    #Neutral mentions
    with col2:
        dig_neutral = st.number_input("Quantidade de **:orange-background[Menções Neutras]**", value=curr_dig_neutral, format="%d", key='_dig_neu')
        st.write("Neutras:", dig_neutral)
    #Negative mentions
    with col3:
        dig_negative = st.number_input("Quantidade de **:red-background[Menções Negativas]**", value=curr_dig_negative, format="%d", key='_dig_neg')
        st.write("Negativas:", dig_negative)


# mask_show_button = not(dig_positive and dig_neutral and dig_negative)

save_dig = st.button("Salvar",)# disabled=mask_show_button)

if save_dig:
    st.session_state['dig_mentions'] = {
        'dig_pos': st.session_state['_dig_pos'],
        'dig_neu': st.session_state['_dig_neu'],
        'dig_neg': st.session_state['_dig_neg'],
    }


    #### Navigation buttons ###
    # st.markdown("-----")
    nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
    with nav_prev:
        st.page_link("views/user_login.py", label="Voltar")
    with nav_next:
        st.page_link("views/press_mentions_page.py", label="Avançar",)
