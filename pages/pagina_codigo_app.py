import streamlit as st

if "logado" not in st.session_state or not st.session_state.logado:
    st.error("Você precisa estar logado para acessar esta página.")
    st.stop()


st.set_page_config(layout="wide")
st.title("Página de Códigos")

# Inicializa os "flags" de mostrar mais
for i in range(1, 5):
    if f"mostrar{i}" not in st.session_state:
        st.session_state[f"mostrar{i}"] = False

# Primeira linha de imagens
col1, col2, col3 = st.columns(3)
with col1:
    st.image("image.png")
with col2:
    st.image("image2.png")
with col3:
    st.image("image3.png")

# Botão: Mostrar mais 1
if st.button("Mostrar mais 1"):
    st.session_state.mostrar1 = True

if st.session_state.mostrar1:
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("image4.png")
    with col5:
        st.image("image5.png")
    with col6:
        st.image("image6.png")

    if st.button("Mostrar mais 2"):
        st.session_state.mostrar2 = True

if st.session_state.mostrar2:
    col7, col8, col9 = st.columns(3)
    with col7:
        st.image("image7.png")
    with col8:
        st.image("image8.png")
    with col9:
        st.image("image9.png")

    if st.button("Mostrar mais 3"):
        st.session_state.mostrar3 = True

if st.session_state.mostrar3:
    col10, col11, col12 = st.columns(3)
    with col10:
        st.image("image10.png")
    with col11:
        st.image("image11.png")
    with col12:
        st.image("image12.png")

    if st.button("Mostrar mais 4"):
        st.session_state.mostrar4 = True

if st.session_state.mostrar4:
    col13, col14, col15 = st.columns(3)
    with col13:
        st.image("image13.png")
    with col14:
        st.image("image14.png")
    with col15:
        st.image("image15.png")
