import streamlit as st
### Data Sanity check ###

if 'user_data' in st.session_state:
    user_data = st.session_state['user_data']
    #dig_mentions = st.session_state['dig_mentions']
    #press_mentions = st.session_state['press_mentions']
else:
    user_data = None

# st.markdown("#### :blue[Confirme os dados a serem inseridos no sistema. Caso estejam corretos, pressione Enviar:]")

# col_review, col_check = st.columns([0.6, 0.4], vertical_alignment='top')
# try:
#     with col_review:
#         format_string = """ 
#         Usuário: {}\n
#         Email: {}\n 
#         Empresa: {}\n 
#         Praça: {}\n 
#         Termômetro Imprensa: {}\n 
#         Termômetro Digital: {}\n 
#         Pontos Positivos: {}\n 
#         Pontos de Atenção: {}"""       
#         st.markdown(format_string.format(user_data['id'], user_data['email'], user_data['business'], user_data['place'], "x", "x", "x", "x" ))
# except Exception as e:
#     st.markdown("Dados incompletos ou não inseridos")

# with col_check:
#     #if 'user data' in st.session_state:
#     #    st.write("Id do usuário atual:", st.session_state["user_data"]["id"])

#     user_ok = st.checkbox("Dados do Usuário")
#     digital_ok = st.checkbox("Dados Termômetro Digital")
#     press_ok = st.checkbox("Dados Termômetro Imprensa")
#     mask_show_button = not(user_ok and digital_ok and press_ok) 
#     send_button = st.button("Enviar", disabled=mask_show_button)

#     if send_button:
#         st.markdown("Dados enviados com sucesso!")


try:
    with st.form('check_data_form'):
        st.write(st.session_state['user_data'])
        st.write(st.session_state['press_mentions'])
        st.write(st.session_state['dig_mentions'])
        st.write(st.session_state['text_notes'])

        check_ok = st.checkbox('Confirmo que li o formulário acima e que os dados estão corretos.')
        send_button = st.form_submit_button("Enviar")
        if send_button:
            if not check_ok:
                st.write("Faltou clicar na caixinha de li e aceito")
            else:
                st.write("Dados enviados com sucesso!")

except:
    st.write("Erro ao recuperar dados do termômetro, preencha novamente os campos.")




#### Navigation buttons ###

st.markdown("-----")
nav_prev, nav_next = st.columns(2, vertical_alignment='bottom')
with nav_prev:
    st.page_link("views/text_entry_page.py", label="Voltar")
#with nav_next:
#    st.page_link("views/text_entry_page.py", label="Avançar", disabled=True)