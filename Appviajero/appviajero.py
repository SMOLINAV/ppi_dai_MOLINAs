import streamlit as st
from auth import crear_usuario, iniciar_sesion
from dashboard import show_dashboard

# Base de datos simulada para almacenar usuarios
usuarios = {"usuario1": "password1", "usuario2": "password2"}

# Título de la aplicación
st.title("APP VIAJEROFELIZ - Planificador de Viajes")

# Sección de "Iniciar Sesión" o "Registrarse"
st.sidebar.title("Autenticación")
opcion_autenticacion = st.sidebar.radio("Selecciona una opción:", ("Iniciar Sesión", "Registrarse"))

if opcion_autenticacion == "Iniciar Sesión":
    usuario = iniciar_sesion(usuarios)
    if usuario:
        show_dashboard(usuario)

elif opcion_autenticacion == "Registrarse":
    crear_usuario(usuarios)

# Sección "Acerca de mí"
st.sidebar.title("Acerca de")
st.sidebar.write("Mi nombre es Santiago Molina Velasquez. Soy estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia. Me apasiona el mundo de la tecnología y estoy comprometido a brindar soluciones innovadoras a través del desarrollo de software y la ingeniería de sistemas.")
