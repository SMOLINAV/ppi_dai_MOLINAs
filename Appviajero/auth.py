import streamlit as st # type: ignore
registered_users = {}

def register_user():
    """
    Registra un nuevo usuario en el sistema.
    
    Args:
        new_username (str): El nombre de usuario del nuevo usuario.
        new_password (str): La contraseña del nuevo usuario.

    Returns:
        None
    """
    st.subheader("Registro de usuario")
    new_username = st.text_input("Nuevo usuario")
    new_password = st.text_input("Nueva contraseña", type="password")
    if st.button("Registrarse"):
        if new_username in registered_users:
            st.error("El usuario ya existe. Por favor, elige otro.")
        else:
            registered_users[new_username] = new_password
            st.success("Usuario registrado exitosamente. Por favor,\
            inicia sesión.")


def change_password():
    """
    Cambia la contraseña de un usuario existente.
    
    Args: None

    Returns:
        None
    """
    st.subheader("Cambio de contraseña")
    user = st.text_input("Usuario:")
    contraseña_actual = st.text_input("Contraseña actual:", type="password")
    nueva_contraseña = st.text_input("Nueva contraseña:", type="password")

    if st.button("Actualizar"):
        if user in registered_users:
            if registered_users[user] == contraseña_actual:
                registered_users[user] = nueva_contraseña
                st.success("¡Contraseña actualizada con éxito!")
            else:
                st.error("Contraseña incorrecta")
        else:
            st.error("Usuario no registrado")

def login_user():
    """
    Iniciar sesión de usuario.

    Args: None'

    Returns:  True si el inicio de sesión fue exitoso, False en caso contrario.
    """
    st.subheader("Iniciar sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if username in registered_users:
            if registered_users[username] == password:
                st.success("Inicio de sesión exitoso. ¡Bienvenido, {}!"
                .format(username))    
                return True
            else:
                st.error("Contraseña incorrecta")
        else:
            st.error("Usuario no registrado")
    return False