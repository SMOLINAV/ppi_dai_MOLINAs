import streamlit as st # type: ignore
import auth
import calculoprecio


from auth import cargar_usuarios, crear_usuario, iniciar_sesion, cambiar_contraseña
from busqueda_colombia import buscar_lugares_ciudad
from busquedaciudadpais import buscar_lugares_ciudad_pais


# Cargar usuarios al iniciar la aplicación
usuarios = auth.cargar_usuarios()

# Panel flotante para el tratamiento de datos
st.sidebar.title("Tratamiento de Datos")

# Enlaces a términos y condiciones y política de privacidad
terms_link = "https://www.freeprivacypolicy.com/live/8924ce9c-3360-4c2d-88f6-9ca4587e1e13"
privacy_link = "https://www.freeprivacypolicy.com/live/4faa307d-9cd8-427b-a9f5-84381e67f8d2"

# Texto de los enlaces
terms_text = "Consultar los términos y condiciones"
privacy_text = "Consultar la política de privacidad"

# Renderizar los enlaces como texto HTML
terms_html = f'<a href="{terms_link}" target="_blank">{terms_text}</a>'
privacy_html = f'<a href="{privacy_link}" target="_blank">{privacy_text}</a>'

# Mostrar los enlaces en el panel lateral
st.sidebar.markdown(terms_html, unsafe_allow_html=True)
st.sidebar.markdown(privacy_html, unsafe_allow_html=True)

# Casilla de verificación para aceptar los términos
acepto_terminos = st.sidebar.checkbox("Acepto los términos y condiciones")

# Verificación de aceptación
if acepto_terminos:
    st.sidebar.success("¡Gracias por aceptar los términos y condiciones!")
else:
    st.sidebar.warning("Debes aceptar los términos y condiciones para acceder a la web.")
    st.stop()

# Sección de autenticación en el panel lateral
st.sidebar.header("Autenticación")

# Opciones de autenticación
opcion_autenticacion = st.sidebar.selectbox("Selecciona una opción:", ["Inicio", "Registrarse", "Cambiar Contraseña"])

# Procesar la opción seleccionada
if opcion_autenticacion == "Inicio":
    usuario = auth.iniciar_sesion()
    if usuario:
        st.session_state.usuario = usuario  # Guardar el usuario en la sesión

elif opcion_autenticacion == "Registrarse":
    auth.crear_usuario(usuarios)

elif opcion_autenticacion == "Cambiar Contraseña":
    if "usuario" in st.session_state:
        auth.cambiar_contraseña(st.session_state.usuario)
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


# Sección "Calcular Tiempo Promedio De Vuelo"
st.header("Calcular Tiempo Promedio De Vuelo")
if "usuario" in st.session_state:
    # Función para calcular el tiempo de vuelo promedio
    def calcular_tiempo_vuelo_promedio(distancia_km, velocidad_promedio_kmh):
        # Convertir la velocidad de km/h a km/min
        velocidad_promedio_kmmin = velocidad_promedio_kmh / 60.0
        # Calcular el tiempo de vuelo promedio en minutos
        tiempo_vuelo_promedio_min = distancia_km / velocidad_promedio_kmmin
        # Convertir el tiempo de vuelo promedio a horas
        tiempo_vuelo_promedio_horas = tiempo_vuelo_promedio_min / 60.0
        return tiempo_vuelo_promedio_horas

    # Sección para ingresar la distancia
    distancia_km = st.number_input("Ingrese la distancia entre los dos puntos en kilómetros:", min_value=0.0, step=1.0)

    # Velocidad promedio de un avión en kilómetros por hora
    velocidad_promedio_kmh = 800

    # Botón para calcular el tiempo de vuelo promedio
    if st.button("Calcular Tiempo de Vuelo Promedio"):
        tiempo_vuelo_promedio = calcular_tiempo_vuelo_promedio(distancia_km, velocidad_promedio_kmh)
        st.write("El tiempo de vuelo promedio es:", tiempo_vuelo_promedio, "horas")

else:
    st.write("Por favor, inicia sesión para acceder a la función para calcular el tiempo de vuelo promedio.")

# Sección para calcular el precio de vuelos
calculoprecio.mostrar_calculo_precio()

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
