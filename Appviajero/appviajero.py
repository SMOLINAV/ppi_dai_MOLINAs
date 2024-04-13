import streamlit as st
from auth import crear_usuario, iniciar_sesion
from dashboard import show_dashboard

# Base de datos simulada para almacenar usuarios
usuarios = {"usuario1": "password1", "usuario2": "password2"}

# Título de la aplicación
st.title("APP VIAJEROFELIZ - Planificador de Viajes")

# Pestañas de la aplicación
tabs = st.sidebar.radio("Menú:", ("Acerca de", "Inicio de Sesión", "Crear Usuario"))

if tabs == "Acerca de":
    st.subheader("Acerca del Creador")
    st.write("Mi nombre es Santiago Molina Velasquez. Soy estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia. Me apasiona el mundo de la tecnología y estoy comprometido a brindar soluciones innovadoras a través del desarrollo de software y la ingeniería de sistemas.")

elif tabs == "Inicio de Sesión":
    usuario = iniciar_sesion(usuarios)
    if usuario:
        show_dashboard(usuario)

elif tabs == "Crear Usuario":
    crear_usuario(usuarios)