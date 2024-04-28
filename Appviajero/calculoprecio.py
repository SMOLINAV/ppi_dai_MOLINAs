import streamlit as st # type: ignore

def mostrar_calculo_precio():
    # Título de la sección
    st.header("Cálculo de Precio de Vuelos")

    # Mensaje introductorio
    st.write("¿Deseas ver el precio de los vuelos en avión?")
    st.write("Aquí está tu solución:")

    # Enlace al servicio de vuelos de Google
    url_vuelos_google = "https://www.google.com/travel/flights?hl=es"

    # Botón para seguir el enlace
    if st.button("Seguir este enlace"):
        js = f"window.open('{url_vuelos_google}')"  # JavaScript para abrir una nueva pestaña con la URL
        html = f'<img src onerror="{js}">'  # Imagen invisible que desencadena la apertura de la URL
        st.markdown(html, unsafe_allow_html=True)

# Ejecutar la función si se ejecuta este script directamente
if __name__ == "__main__":
    mostrar_calculo_precio()