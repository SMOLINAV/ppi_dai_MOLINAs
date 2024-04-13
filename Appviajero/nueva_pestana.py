import streamlit as st

def mostrar_pagina_busqueda():
    st.title("Busca tu próximo destino")
    
    # Elemento para escribir el próximo destino
    proximo_destino = st.text_input("Escribe tu próximo destino")

    # Botón para realizar la búsqueda
    if st.button("Buscar"):
        # Aquí puedes agregar la lógica para realizar la búsqueda del destino
        st.write(f"Buscando información sobre {proximo_destino}...")
