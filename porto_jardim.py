import streamlit as st

def mostrar_porto_jardim():
    """
    Página de Previsão - Porto Alegre Jardim.
    """
    # Caminho para o logo
    logo_path = "logo.png"

    # Adicionar o logo na sidebar
    with st.sidebar:
        col1, col2, col3 = st.columns([1, 3, 1])  # Centralizar o logo
        with col2:
            st.image(logo_path, width=150)

    # Adicionar título com logo ao lado
    col1, col2 = st.columns([1, 5.5])
    with col1:
        st.image(logo_path, width=100)
    with col2:
        st.markdown(
            """
            <h1 style='font-size: 36px; margin: 0; line-height: 1.2;'>
                Previsão - Porto Alegre Jardim
            </h1>
            """,
            unsafe_allow_html=True
        )

    