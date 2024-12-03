import streamlit as st

st.markdown("## :pencil: :blue[Observações]")
st.markdown("Insira nos campos abaixo observações relevantes do dia")

placeholder_txt = "Insira aqui seu texto. Pontos diferentes devem ser separados por ponto e vírgula;"

if ('text_pos', 'text_warn') in st.session_state.keys():
    curr_text_pos = st.session_state['text_pos']
    curr_text_warn = st.session_state['text_warn']
else:
    curr_text_pos = dict(press=None, dig=None)
    curr_text_warn = dict(press=None, dig=None)


with st.container(border=True):
    with st.expander(":iphone: Digital"):
        col1, col2 = st.columns(2)
        with col1:
            txt_pos = st.text_area(
                ":green-background[Pontos Positivos]",
                curr_text_pos['dig'], placeholder=placeholder_txt, key="_pos_dig"
            )

        with col2:
            txt_warn = st.text_area(
                ":orange-background[Pontos de Atenção]",
                curr_text_warn['dig'], placeholder=placeholder_txt, key="_warn_dig"
            )


    with st.expander(":newspaper: Imprensa"):
        col1, col2 = st.columns(2)
        with col1:
            txt_pos = st.text_area(
                ":green-background[Pontos Positivos]",
                curr_text_pos['press'], placeholder=placeholder_txt, key="_pos_press"
            )

        with col2:
            txt_warn = st.text_area(
                ":orange-background[Pontos de Atenção]",
                curr_text_warn['press'], placeholder=placeholder_txt, key="_warn_press"
            )
    
mask_show_button = not(txt_pos and txt_warn)

save_text = st.button("Salvar", disabled=mask_show_button)

if save_text:
    st.session_state["text_pos"]= dict(press=st.session_state['_pos_press'], dig=st.session_state['_pos_dig'])
    st.session_state["text_warn"]= dict(press=st.session_state['_warn_press'], dig=st.session_state['_warn_dig'])

    #### Navigation buttons ###
    # st.markdown("-----")
    nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
    with nav_prev:
        st.page_link("views/press_mentions_page.py", label="Voltar")
    with nav_next:
        st.page_link("views/data_review_page.py", label="Avançar",)