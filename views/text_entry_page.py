import streamlit as st

st.markdown("## :pencil: :blue[Observações]")
st.markdown("Insira nos campos abaixo observações relevantes do dia")

placeholder_txt = "Insira aqui seu texto. Pontos diferentes devem ser separados por ponto e vírgula;"

if 'text_notes' in st.session_state:
    curr_txt_pos = st.session_state['text_notes']['txt_pos']
    curr_txt_warn = st.session_state['text_notes']['txt_warn']
else:
    curr_txt_pos = None
    curr_txt_warn = None

with st.expander(":iphone: Digital"):
    col1, col2 = st.columns(2)
    with col1:
        txt_pos = st.text_area(
            ":green-background[Pontos Positivos]",
            curr_txt_pos, placeholder=placeholder_txt, key="_ppos_dig"
        )
        # offer some user tagging for the positive news
        # tags_pos = ""

    with col2:
        txt_warn = st.text_area(
            ":orange-background[Pontos de Atenção]",
            curr_txt_warn, placeholder=placeholder_txt, key="_pat_dig"
        )
    # offer some user tagging for the positive news
    # tags_warn = ""

with st.expander(":newspaper: Imprensa"):
    col1, col2 = st.columns(2)
    with col1:
        txt_pos = st.text_area(
            ":green-background[Pontos Positivos]",
            curr_txt_pos, placeholder=placeholder_txt, key="_ppos_imp"
        )
        # offer some user tagging for the positive news
        # tags_pos = ""

    with col2:
        txt_warn = st.text_area(
            ":orange-background[Pontos de Atenção]",
            curr_txt_warn, placeholder=placeholder_txt, key="_pat_imp"
        )
    # offer some user tagging for the positive news
    # tags_warn = ""

#st.write(f"You wrote {len(txt_pos) + len(txt_warn)} characters.")

mask_show_button = not(txt_pos and txt_warn)

save_text = st.button("Salvar", disabled=mask_show_button)

if save_text:
    st.session_state['text_notes'] = {
        "txt_pos": dict(imp=st.session_state['_ppos_imp'], dig=st.session_state['_ppos_dig']),
        "txt_warn": dict(imp=st.session_state['_pat_imp'], dig=st.session_state['_pat_dig']),
        }


#### Navigation buttons ###

st.markdown("-----")
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
with nav_prev:
    st.page_link("views/press_mentions_page.py", label="Voltar")
with nav_next:
    st.page_link("views/data_review_page.py", label="Avançar",)