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

# Sección "Acerca de mí"
    st.header("Acerca de Mí")
    st.write('''Mi nombre es Santiago Molina Velasquez y soy estudiante 
             de ingeniería de sistemas en la Universidad Nacional de Colombia. 
             Me apasiona el mundo de la tecnología y estoy comprometido a brindar soluciones 
             innovadoras a través del desarrollo de software y la ingeniería de sistemas. 
             Tengo como metas cercanas terminar mi carrera profesional y seguir 
             consolidandome y laborando en todo lo relacionado a tecnología y 
             en el gran mundo del internet.''')
    st.write("Puedes contactarme en smolinav@unal.edu.co")