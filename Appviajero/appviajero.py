import streamlit as st
from auth import crear_usuario, iniciar_sesion
from dashboard import show_dashboard

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
        show_dashboard(usuario)
