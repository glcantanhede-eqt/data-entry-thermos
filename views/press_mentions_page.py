import streamlit as st

st.markdown("## :newspaper: :blue[Termômetro Imprensa]")

# Initializing the session state
if 'press_mentions' in st.session_state:
    curr_press_positive = st.session_state['press_mentions']['press_pos']
    curr_press_negative = st.session_state['press_mentions']['press_neg']
else:
    curr_press_positive = 0
    curr_press_negative = 0

with st.container(border=True):
    # Data entry part for Press media
    col1, col2 = st.columns(2)
    #Positive mentions
    with col1:
        press_positive = st.number_input("**Quantidade de :green-background[Notícias Positivas]**", value=curr_press_positive, format="%d", key='_press_pos')
        st.write("Positivas:", press_positive)

    #Negative mentions
    with col2:
        press_negative = st.number_input("**Quantidade de :red-background[Notícias Negativas]**", value=curr_press_negative, format="%d", key='_press_neg')
        st.write("Negativas:", press_negative)


# mask_show_button = not(press_positive and press_negative)
save_press = st.button("Salvar")#, disabled=mask_show_button)

if save_press:
    st.session_state['press_mentions'] = {
        'press_pos': st.session_state['_press_pos'],
        'press_neg': st.session_state['_press_neg'],
    }



    #### Navigation buttons ###
    # st.markdown("-----")
    nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
    with nav_prev:
        st.page_link("views/digital_mentions_page.py", label="Voltar")
    with nav_next:
        st.page_link("views/text_entry_page.py", label="Avançar",)