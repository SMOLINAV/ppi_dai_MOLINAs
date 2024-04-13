import streamlit as st

# Base de datos simulada para almacenar usuarios
usuarios = {"usuario1": "password1", "usuario2": "password2"}

# Título de la aplicación
st.title("Sistema de Registro e Inicio de Sesión")

# Opción para seleccionar acción (registro o inicio de sesión)
opcion = st.radio("Selecciona una opción:", ("Crear un nuevo usuario", "Iniciar sesión"))

# Manejo de la opción seleccionada
if opcion == "Crear un nuevo usuario":
    st.header("Crear Nuevo Usuario")
    nuevo_usuario = st.text_input("Nombre de usuario")
    nueva_contraseña = st.text_input("Contraseña", type="password")

    if st.button("Registrar"):
        if nuevo_usuario in usuarios:
            st.error("El usuario ya existe. Por favor, elige otro nombre de usuario.")
        else:
            usuarios[nuevo_usuario] = nueva_contraseña
            st.success("Usuario creado exitosamente. ¡Ahora puedes iniciar sesión!")

elif opcion == "Iniciar sesión":
    st.header("Iniciar Sesión")
    usuario = st.text_input("Nombre de usuario")
    contraseña = st.text_input("Contraseña", type="password")

    if st.button("Iniciar Sesión"):
        if usuario not in usuarios:
            st.error("Usuario no encontrado. Por favor, registra una cuenta.")
        elif usuarios[usuario] != contraseña:
            st.error("Contraseña incorrecta. Por favor, inténtalo de nuevo.")
        else:
            st.success(f"Bienvenido, {usuario}! Has iniciado sesión exitosamente.")

# Crear pestaña para información del creador
if st.button("Información del Creador"):
    st.header("Acerca de Mí")
    st.write("¡Hola! Mi nombre es Santiago Molina Velasquez y soy estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia. Me apasiona el mundo de la tecnología y estoy comprometido a brindar soluciones innovadoras a través del desarrollo de software y la ingeniería de sistemas. Tengo como metas cercanas terminar mi carrera profesional y seguir consolidandome y laborando en todo lo relacionado a tecnología y en el gran mundo del internet.")
    st.write("Puedes contactarme en smolinav@unal.edu.co")
