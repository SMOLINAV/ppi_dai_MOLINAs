import streamlit as st

def calcular_duracion_vuelo():
    # Entrada de distancia en kilómetros
    distancia_km = st.number_input("Ingrese la distancia entre los dos puntos en kilómetros:", min_value=0.0, step=1.0)

    # Velocidad promedio de un avión en kilómetros por hora
    velocidad_promedio_kmh = 800

    # Botón para calcular la duración del vuelo
    if st.button("Calcular Duración del Vuelo"):
        duracion_vuelo = distancia_km / velocidad_promedio_kmh
        st.write("Duración del vuelo:", duracion_vuelo, "horas")
