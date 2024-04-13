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
            # Redirige al usuario a la página "Busca tu próximo destino"
            st.redirect("busca_destino.py")
