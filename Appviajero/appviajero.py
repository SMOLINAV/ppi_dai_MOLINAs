from Appviajero.about_me import show_about_me
import streamlit as st
from auth import crear_usuario, iniciar_sesion
from dashboard import show_dashboard

# Base de datos simulada para almacenar usuarios
usuarios = {"usuario1": "password1", "usuario2": "password2"}

# Título de la aplicación
st.title("APP VIAJEROFELIZ - Planificador de Viajes")

# Sección de "Iniciar Sesión" o "Registrarse"
st.header("Autenticación")
opcion_autenticacion = st.radio("Selecciona una opción:", ("Iniciar Sesión", "Registrarse"))

if opcion_autenticacion == "Iniciar Sesión":
    usuario = iniciar_sesion(usuarios)
    if usuario:
        show_dashboard(usuario)

elif opcion_autenticacion == "Registrarse":
    crear_usuario(usuarios)

show_about_me()