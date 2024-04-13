import streamlit as st
from user_info import show_user_info
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
    iniciar_sesion(usuarios)

# Mostrar información del usuario
if st.button("Mostrar Información del Usuario"):
    show_user_info(usuarios)
