import streamlit as st

st.markdown("## :pencil: :blue[Observações]")
st.markdown("Insira nos campos abaixo observações relevantes do dia")

placeholder_txt = "Insira aqui seu texto. Pontos diferentes devem ser separados por ponto e vírgula;"

if ('text_imp', 'text_dig') in st.session_state.keys():
    curr_text_imp = st.session_state['text_imp']
    curr_text_dig = st.session_state['text_dig']
else:
    curr_text_imp = dict(pros=None, warn=None)
    curr_text_dig = dict(pros=None, warn=None)

with st.expander(":iphone: Digital"):
    col1, col2 = st.columns(2)
    with col1:
        txt_pos = st.text_area(
            ":green-background[Pontos Positivos]",
            curr_text_dig['pros'], placeholder=placeholder_txt, key="_pros_dig"
        )
        # offer some user tagging for the positive news
        # tags_pos = ""

    with col2:
        txt_warn = st.text_area(
            ":orange-background[Pontos de Atenção]",
            curr_text_dig['warn'], placeholder=placeholder_txt, key="_warn_dig"
        )
    # offer some user tagging for the positive news
    # tags_warn = ""

with st.expander(":newspaper: Imprensa"):
    col1, col2 = st.columns(2)
    with col1:
        txt_pos = st.text_area(
            ":green-background[Pontos Positivos]",
            curr_text_imp['pros'], placeholder=placeholder_txt, key="_pros_imp"
        )
        # offer some user tagging for the positive news
        # tags_pos = ""

    with col2:
        txt_warn = st.text_area(
            ":orange-background[Pontos de Atenção]",
            curr_text_imp['warn'], placeholder=placeholder_txt, key="_warn_imp"
        )
    # offer some user tagging for the positive news
    # tags_warn = ""

#st.write(f"You wrote {len(txt_pos) + len(txt_warn)} characters.")

mask_show_button = not(txt_pos and txt_warn)

save_text = st.button("Salvar", disabled=mask_show_button)

if save_text:
    st.session_state["text_imp"]= dict(pros=st.session_state['_pros_imp'], warn=st.session_state['_warn_imp'])
    st.session_state["text_dig"]= dict(pros=st.session_state['_pros_dig'], warn=st.session_state['_warn_dig'])


#### Navigation buttons ###

st.markdown("-----")
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
with nav_prev:
    st.page_link("views/press_mentions_page.py", label="Voltar")
with nav_next:
    st.page_link("views/data_review_page.py", label="Avançar",)