import streamlit as st

# Intenta importar las funciones necesarias desde el módulo auth.py
try:
    from auth import crear_usuario, iniciar_sesion
except ImportError:
    # Maneja el error de importación aquí
    st.error("Error al importar las funciones desde auth.py. Verifica la ubicación del archivo.")

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
