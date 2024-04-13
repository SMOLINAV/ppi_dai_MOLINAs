import streamlit as st

def crear_usuario(usuarios):
    st.header("Crear Nuevo Usuario")
    nuevo_usuario = st.text_input("Nombre de usuario")
    nueva_contraseña = st.text_input("Contraseña", type="password")

    if st.button("Registrar"):
        if nuevo_usuario in usuarios:
            st.error("El usuario ya existe. Por favor, elige otro nombre de usuario.")
        else:
            usuarios[nuevo_usuario] = nueva_contraseña
            st.success("Usuario creado exitosamente. ¡Ahora puedes iniciar sesión!")

def iniciar_sesion(usuarios):
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
            # Redirige al usuario a la nueva pestaña
            st.set_page_config(page_title="¿Qué destino buscas?")
            st.write("# ¿Qué destino buscas?")
            st.write("¡Bienvenido! Utiliza esta página para buscar tu próximo destino.")
            # También puedes agregar más contenido aquí si lo deseas
            st.write("Por favor, actualiza la página si no se redirige automáticamente.")