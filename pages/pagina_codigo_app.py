import streamlit as st

st.set_page_config(layout="wide")  # Melhor para colunas

# Página "Códigos"
st.title("Página de Códigos")

# Primeira linha de imagens
col1, col2, col3 = st.columns(3)
with col1:
    st.image("image.png")
with col2:
    st.image("image2.png")
with col3:
    st.image("image3.png")

# Mostrar mais 1
if st.button("Mostrar mais 1"):
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("image4.png")
    with col5:
        st.image("image5.png")
    with col6:
        st.image("image6.png")

    # Mostrar mais 2 (dentro do 1)
    if st.button("Mostrar mais 2"):
        col7, col8, col9 = st.columns(3)
        with col7:
            st.image("image7.png")
        with col8:
            st.image("image8.png")
        with col9:
            st.image("image9.png")

        # Mostrar mais 3 (dentro do 2)
        if st.button("Mostrar mais 3"):
            col10, col11, col12 = st.columns(3)
            with col10:
                st.image("image10.png")
            with col11:
                st.image("image11.png")
            with col12:
                st.image("image12.png")

            # Mostrar mais 4 (último nível)
            if st.button("Mostrar mais 4"):
                col13, col14, col15 = st.columns(3)
                with col13:
                    st.image("image13.png")
                with col14:
                    st.image("image14.png")
                with col15:
                    st.image("image15.png")

