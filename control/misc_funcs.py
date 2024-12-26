import streamlit as st
from time import sleep

# def showProgressBar():
#     progress_text = "Operação em progresso. Aguarde..."
#     my_bar = progress(0, text=progress_text)
#     #time.sleep()
#     for percent_complete in range(100):
#         sleep(0.0001)
#         my_bar.progress(percent_complete + 1, text=progress_text)
#     sleep(1)
#     my_bar.progress(100, text="Operação concluída com sucesso!")
#     sleep(0.1)

def pick_color(value):
    if value < 0.36:
        return "#eb4034" #style.format(color_pick="#eb4034")
    elif value < 0.71:
        return "#ffaa00" #style.format(color_pick="#ffaa00")
    else:
        return "#00b509" #style.format(color_pick="#00b509")

def write_footer():
    st.divider()
    st.markdown(
        """:copyright: _Copyright 2024 - Time Inteligência de Dados_ <br>
        Gerência de Comunicação Externa, Marketing e Sustentabilidade <br>
        Diretoria de Clientes, Serviços e Inovação <br>
        **:blue[Grupo Equatorial]**""",
        unsafe_allow_html=True)
