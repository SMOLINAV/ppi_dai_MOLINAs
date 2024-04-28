import streamlit as st # type: ignore
import json

def cargar_usuarios():
    '''
    esta función carga los usuarios existentes en el archivo 'usuarios.json'
    y los devuelve como un diccionario.
    si el archivo no existe, devuelve un diccionario vacío.
    args:
        None
    returns:
        dict: diccionario de usuarios
    '''
    try:
        with open("usuarios.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def guardar_usuarios(usuarios):
    '''
    esta función escribe los usuarios en el archivo 'usuarios.json'
    args:
        dict: diccionario de usuarios
    returns:
        None
    '''
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)

def crear_usuario():
    '''
    esta función crea un nuevo usuario en el archivo 'usuarios.json'
    args:
        None
    returns:
        None
    '''
    st.header("Crear Nuevo Usuario")
    nuevo_usuario = st.text_input("Nombre de usuario")
    nueva_contraseña = st.text_input("Contraseña", type="password")

    if st.button("Registrar"):
        usuarios = cargar_usuarios()
        if nuevo_usuario in usuarios:
            st.error("El usuario ya existe. Por favor, elige otro nombre de usuario.")
        else:
            usuarios[nuevo_usuario] = nueva_contraseña
            guardar_usuarios(usuarios)
            st.success("Usuario creado exitosamente. ¡Ahora puedes iniciar sesión!")

def iniciar_sesion():
    '''
    esta función inicia la sesión de un usuario existente
    args:
        None
    returns:
        str: nombre de usuario
    '''
    usuarios = cargar_usuarios()
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
            return usuario

def cambiar_contraseña(usuario):
    '''
    esta función cambia la contraseña de un usuario existente
    args:
        str: nombre de usuario
    returns:
        None
    '''
    usuarios = cargar_usuarios()
    if usuario in usuarios:
        st.header("Cambio de Contraseña")
        nueva_contraseña = st.text_input("Nueva Contraseña", type="password")
        if st.button("Cambiar Contraseña"):
            usuarios[usuario] = nueva_contraseña
            guardar_usuarios(usuarios)
            st.success("Contraseña actualizada exitosamente.")
    else:
        st.error("Usuario no encontrado. Por favor, inicia sesión nuevamente.")
