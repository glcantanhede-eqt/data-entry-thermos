import streamlit as st

st.markdown("## :pencil: :blue[Observações]")
st.markdown("Insira nos campos abaixo observações relevantes do dia")

placeholder_txt = "Insira aqui seu texto. Pontos diferentes devem ser separados por ponto e vírgula;"
curr_text_pos = dict(press=None, dig=None)
curr_text_warn = dict(press=None, dig=None)


if ('text_pos', 'text_warn') in st.session_state.keys():
    curr_text_pos = st.session_state['text_pos']
    curr_text_warn = st.session_state['text_warn']



with st.container(border=True):
    with st.expander(":iphone: Digital"):
        col1, col2 = st.columns(2)
        with col1:
            dig_txt_pos = st.text_area(
                label=":green-background[Pontos Positivos]",
                value=curr_text_pos['dig'],max_chars=80, placeholder=placeholder_txt, key="_pos_dig"
            )

        with col2:
            dig_txt_warn = st.text_area(
                label=":orange-background[Pontos de Atenção]",
                value=curr_text_warn['dig'],max_chars=160, placeholder=placeholder_txt, key="_warn_dig"
            )


    with st.expander(":newspaper: Imprensa"):
        col1, col2 = st.columns(2)
        with col1:
            press_txt_pos = st.text_area(
                label=":green-background[Pontos Positivos]",
                value=curr_text_pos['press'],max_chars=80, placeholder=placeholder_txt, key="_pos_press"
            )

        with col2:
            press_txt_warn = st.text_area(
                label=":orange-background[Pontos de Atenção]",
                value=curr_text_warn['press'],max_chars=160, placeholder=placeholder_txt, key="_warn_press"
            )

# This here makes sure the user has at least typed something in the text boxes before pressing save
# TODO Not working in prod, for some reason the logic isn't evaluating
# TODO try using on_change property to set some boolean vars and use them in the mask instead
bool_show_button = (press_txt_pos == "") or (press_txt_warn == "") or (dig_txt_pos == "") or (dig_txt_warn == "")

save_text = st.button("Salvar", disabled=bool_show_button, icon=":material/save:")

if save_text:
    st.session_state["text_pos"]= dict(press=press_txt_pos, dig=dig_txt_pos)
    st.session_state["text_warn"]= dict(press=press_txt_warn, dig=dig_txt_warn)

    #### Navigation buttons ###
    # st.markdown("-----")
    nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
    with nav_prev:
        st.page_link("views/press_mentions_page.py", label="Voltar")
    with nav_next:
        st.page_link("views/data_review_page.py", label="Avançar",)