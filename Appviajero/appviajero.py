import streamlit as st # type: ignore
import pandas as pd
import auth
import terminoscondiciones
import aeropuertos
import codigoiso

from busqueda_colombia import buscar_lugares_departamento
from busquedaciudadpais import buscar_lugares_ciudad_pais

# Título de la aplicación
st.title("APP VIAJEROFELIZ")

# Inicializar el estado si no existe
if 'visible' not in st.session_state:
    st.session_state.visible = False

if 'aceptado' not in st.session_state:
    st.session_state.aceptado = False

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Verificar si el usuario acepta los términos y condiciones
ver_terminos = st.button("Ver Términos y Condiciones")

# Actualización de la variable "visible" según el estado del botón
if ver_terminos:
    st.session_state.visible = not st.session_state.visible

# Mostrar términos y condiciones solo si la variable "visible" es True
if st.session_state.visible and not st.session_state.aceptado:
    terminoscondiciones.terminos_condiciones()
    aceptado = st.checkbox("Acepto los términos y condiciones")
    
    if aceptado:
        st.session_state.aceptado = True
        st.session_state.visible = False
        st.experimental_rerun()

if st.session_state.aceptado:
    
    # Sección de autenticación en el panel lateral
    st.sidebar.header("Autenticación")

    # Opciones de autenticación
    opcion_autenticacion = st.sidebar.selectbox("Selecciona una opción:", ["Inicio", "Iniciar sesión", "Registrarse", "Cambiar Contraseña"])

    # Procesar la opción seleccionada
    if opcion_autenticacion == "Inicio":
        # Título de la aplicación
        st.title("APP VIAJEROFELIZ")

        # Sección de buscar lugares en Colombia
        st.header("Buscar Lugares En Colombia")
        departamento = st.text_input("Ingrese el nombre de un departamento en Colombia:")
        if departamento:
            lugares = buscar_lugares_departamento(departamento)
            if lugares:
                st.write(f"Lugares bonitos e importantes del {departamento}:")
                for lugar in lugares:
                    st.write(f"- {lugar}")
            else:
                st.write("No se encontró ningún departamento en Colombia.")

        # Sección de buscar lugares en países de América
        st.header("Buscar Lugares En América")
        paises = [
            "Argentina", "Brasil", "Canadá", "Chile", "Costa Rica", "Cuba",
            "Estados Unidos", "México",
            "Panamá", "Paraguay", "Perú", "Puerto Rico", "Uruguay", "Venezuela"
        ]
        pais = st.selectbox("Seleccione un país:", sorted(paises))
        if pais:
            ciudades = buscar_lugares_ciudad_pais(pais)
            st.write(f"Ciudades importantes de {pais.capitalize()}:")
            for ciudad, lugares in ciudades.items():
                st.write(f"{ciudad}:")
                for lugar in lugares:
                    st.write(f"- {lugar}")

        # Sección para ver el precio de vuelos
        st.header("Ver Precio De Vuelos")
        if st.button("Ver Precio de Vuelos en Avión"):
            st.write("Encontrarás el link para ir a una página de Google, para poner tu lugar de destino y saber los vuelos que hay disponibles y sus precios")
            st.markdown("https://www.google.com/travel/flights?hl=es")

            # Mostrar secciones solo si el usuario ha iniciado sesión
        if st.session_state.logged_in:
            # Sección de código ISO
            st.header("Código ISO")
            nombrecomun = st.text_input("Ingrese el nombre del país:")
            if st.button("Ver Código ISO"):
                codigonombre = codigoiso.extraer_codigo_iso(nombrecomun)
                if codigonombre:
                    st.write(f"El código ISO alfa-2 de {nombrecomun} es: {codigonombre}")
                else:
                    st.write(f"No se encontró el código ISO alfa-2 para {nombrecomun}.")

            # Sección de Aeropuertos
            st.header("Aeropuertos")
            pais = st.text_input("Ingrese el ISO del país:")
            if st.button("Ver Mapa de Aeropuertos"):
                busque = aeropuertos.buscar_aeropuertos_por_pais(aeropuertos.datos, pais)
                resultado = aeropuertos.graficar_mapa(busque)
                st.plotly_chart(resultado)

        else:
            st.write("Por favor, inicia sesión para acceder a más funcionalidades.")


    elif opcion_autenticacion == "Iniciar sesión":
        if auth.login_user():
            st.session_state.logged_in = True
            st.experimental_rerun()
    elif opcion_autenticacion == "Registrarse":
        auth.register_user()
    elif opcion_autenticacion == "Cambiar Contraseña":
        auth.change_password()


