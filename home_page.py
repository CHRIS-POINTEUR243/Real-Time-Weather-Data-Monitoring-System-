import streamlit as st
from datetime import datetime
from porto_aeroporto import porto_aeroporto
from porto_belem import porto_belem
from porto_porto import porto_porto
from porto_jardim import mostrar_porto_jardim
from banco_dados import banco_dados
from equipe import equipe

def home_page():
    """
    Página inicial com a mensagem de boas-vindas e o menu lateral.
    """

    # Caminho para o logo
    logo_path = "logo.png"

    # Menu lateral
    menu = st.sidebar.selectbox(
        "Menu",
        ["Home", "Previsão", "Banco de Dados", "Equipe"]
    )

    if menu == "Previsão":
        # Submenu de Previsão
        operacao = st.sidebar.selectbox(
            "Selecione a operação:",
            [
                "Porto Alegre Aeroporto",
                "Porto Alegre Belem",
                "Porto Alegre Jardim",
                "Porto Alegre Porto"
            ]
        )

        # Redirecionar para o conteúdo da operação selecionada
        if operacao == "Porto Alegre Aeroporto":
            porto_aeroporto()  # Apenas o conteúdo do arquivo porto_aeroporto.py
        elif operacao == "Porto Alegre Belem":
            porto_belem()  # Apenas o conteúdo do arquivo porto_belem.py
        elif operacao == "Porto Alegre Jardim":
            mostrar_porto_jardim()  # Apenas o conteúdo do arquivo porto_jardim.py
        elif operacao == "Porto Alegre Porto":
            porto_porto()  # Apenas o conteúdo do arquivo porto_porto.py

    elif menu == "Home":
        # Conteúdo da Home
        # Adicionar o logo na sidebar
        with st.sidebar:
            col1, col2, col3 = st.columns([1, 3, 1])  # Centralizar o logo
            with col2:
                st.image(logo_path, width=150)

        # Adicionar título e mensagem de boas-vindas
        col1, col2 = st.columns([1, 5.5])
        with col1:
            st.image(logo_path, width=100)
        with col2:
            st.markdown(
                """
                <h1 style='font-size: 42px; margin: 0; line-height: 1.2;'>
                    Sistema de Laboratório LMQA
                </h1>
                """,
                unsafe_allow_html=True
            )
        st.success("Bem-vindo ao sistema de previsão do Laboratório LMQA!")

        # 🕒 Exibir data e hora como métricas
        col1, col2 = st.columns(2)
        col1.metric("Data", datetime.now().strftime('%d/%m/%Y'))
        col2.metric("Hora", datetime.now().strftime('%H:%M:%S'))

    elif menu == "Banco de Dados":
        banco_dados()  # Chamando a função correspondente

    elif menu == "Equipe":
        equipe()  # Chamando a função correspondente
