import streamlit as st # type: ignore
import auth
import terminoscondiciones

from busqueda_colombia import buscar_lugares_ciudad
from busquedaciudadpais import buscar_lugares_ciudad_pais

# Título de la aplicación
st.title("APP VIAJEROFELIZ")

# Inicializar el estado si no existe
if 'visible' not in st.session_state:
    st.session_state.visible = False

if 'aceptado' not in st.session_state:
    st.session_state.aceptado = False

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
    opcion_autenticacion = st.sidebar.selectbox("Selecciona una opción:", ["Inicio", "iniciar sesión", "Registrarse", "Cambiar Contraseña"])
    # Procesar la opción seleccionada
    if opcion_autenticacion == "Inicio":
        # Título de la aplicación
        st.title("APP VIAJEROFELIZ")


        # Seccion buscar lugares Colombia
        st.header("Buscar Lugares En Colombia")
        ciudad = st.text_input("Ingrese el nombre de una ciudad colombiana:")
        if ciudad:
            lugares = buscar_lugares_ciudad(ciudad)
            st.write(f"Lugares bonitos e importantes de {ciudad.capitalize()}:")
            for lugar in lugares:
                st.write(f"- {lugar}")


        # Seccion buscar lugares paises América
        st.header("Buscar Lugares En América")
        if "usuario" in st.session_state:
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

        else:
            st.write("Por favor, inicia sesión para acceder a la función de busqueda en paises de América.")


        # Sección para ver el precio de vuelos
        st.header("Ver Precio De Vuelos")
        if "usuario" in st.session_state:
            if st.button("Ver Precio de Vuelos en Avión"):
                st.write("Encontrarás el link para ir a una pagina de google, para poner tu lugar de destino y saber los vuelos que hay disponibles y sus precios")
                st.markdown("https://www.google.com/travel/flights?hl=es")
        else:
            st.write("Por favor, inicia sesión para acceder a la función para calcular el precio de vuelos.")


        # Sección "Acerca de mí"
        st.write("<span style='color:green'>Acerca De Mí</span>", unsafe_allow_html=True)
        st.write('''Mi nombre es Santiago Molina Velasquez y soy estudiante 
                    de ingeniería de sistemas en la Universidad Nacional de Colombia. 
                    Me apasiona el mundo de la tecnología y estoy comprometido a brindar soluciones 
                    innovadoras a través del desarrollo de software y la ingeniería de sistemas. 
                    Tengo como metas cercanas terminar mi carrera profesional y seguir 
                    consolidándome y laborando en todo lo relacionado a tecnología y 
                    en el gran mundo del internet.''')
        st.write("Puedes contactarme smolinav@unal.edu.co")

    elif opcion_autenticacion == "iniciar sesión":
        auth.login_user()
    elif opcion_autenticacion == "Registrarse":
        crear_usuario()

    elif opcion_autenticacion == "Cambiar Contraseña":
        if "usuario" in st.session_state:
            cambiar_contraseña(st.session_state.usuario)


