import streamlit as st
from login import login
from home_page import home_page

def main():
    """
    Função principal que gerencia a navegação entre as páginas.
    """
    # Verifica o status de login
    if "login_status" not in st.session_state:
        st.session_state.login_status = False

    # Se estiver logado, redireciona para a Home Page
    if st.session_state.login_status:
        home_page()
    else:
        login()

if __name__ == "__main__":
    main()
