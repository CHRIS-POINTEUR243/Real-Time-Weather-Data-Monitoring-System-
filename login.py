import streamlit as st
import time

def login():
    """
    Tela de login com carregamento após o login.
    """
    # Caminho para o logo
    logo_path = "logo.png"

    # Cabeçalho com logo no centro superior
    col1, col2, col3 = st.columns([3, 4, 3])
    with col2:  # Centralizar e aumentar o logo
        st.image(logo_path, width=250)  # Ajuste o tamanho aqui

    # Título da página
    st.title("Login - Sistema LMQA")

    # Inicializa o status de login e o usuário
    if "login_status" not in st.session_state:
        st.session_state.login_status = False
    if "usuario" not in st.session_state:
        st.session_state.usuario = ""

    # Formulário de login
    usuario = st.text_input("Usuário (ID)")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario and senha:
            # Salva o nome do usuário na sessão
            st.session_state.usuario = usuario

            st.success(f"Bem-vindo, {usuario}!")

            # Animação de carregamento
            with st.spinner("Carregando o sistema..."):
                time.sleep(2)

            # Define o login como bem-sucedido e redireciona
            st.session_state.login_status = True
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos!")
