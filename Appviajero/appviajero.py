import streamlit as st
from auth import crear_usuario, iniciar_sesion

# Base de datos simulada para almacenar usuarios
usuarios = {"usuario1": "password1", "usuario2": "password2"}

# Título de la aplicación
st.title("Sistema de Registro e Inicio de Sesión")

# Opción para seleccionar acción (registro o inicio de sesión)
opcion = st.radio("Selecciona una opción:", ("Crear un nuevo usuario", "Iniciar sesión"))

# Manejo de la opción seleccionada
if opcion == "Crear un nuevo usuario":
    crear_usuario(usuarios)

elif opcion == "Iniciar sesión":
    usuario = iniciar_sesion(usuarios)
    if usuario:
        # Lógica del dashboard
        st.subheader(f"Bienvenido, {usuario}!")
        st.write("Aquí puedes buscar vuelos, trenes, autobuses y tipos de alojamientos.")
        
        # Agregar funcionalidad de búsqueda
        with st.expander("Buscar"):
            tipo_busqueda = st.selectbox("Selecciona el tipo de búsqueda:", ("Vuelos", "Trenes", "Autobuses", "Alojamientos"))
            if tipo_busqueda == "Vuelos":
                origen = st.text_input("Origen:")
                destino = st.text_input("Destino:")
                fecha_salida = st.date_input("Fecha de salida:")
                fecha_regreso = st.date_input("Fecha de regreso:")
                # Aquí puedes agregar la lógica de búsqueda de vuelos
            elif tipo_busqueda == "Trenes":
                # Lógica de búsqueda de trenes
                pass
            elif tipo_busqueda == "Autobuses":
                # Lógica de búsqueda de autobuses
                pass
            elif tipo_busqueda == "Alojamientos":
                # Lógica de búsqueda de alojamientos
                pass
