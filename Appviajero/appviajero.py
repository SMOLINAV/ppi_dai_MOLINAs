import streamlit as st
from auth import cargar_usuarios, crear_usuario, iniciar_sesion, cambiar_contraseña
from nueva_pestana import mostrar_pagina_busqueda
from busqueda_colombia import buscar_lugares_ciudad
from busquedaciudadpais import buscar_lugares_ciudad_pais

# Cargar usuarios al iniciar la aplicación
usuarios = cargar_usuarios()

# Mantener seccion
def manage_session():
    if 'usuario' not in st.session_state:
        st.session_state.usuario = None

# Título de la aplicación
st.title("APP VIAJEROFELIZ - Planificador de Viajes")

# Manejo de la sesión
manage_session()

# Sección de "Iniciar Sesión" o "Registrarse"
st.header("Autenticación")
opcion_autenticacion = st.radio("Selecciona una opción:", ("Iniciar Sesión", "Registrarse"))

if opcion_autenticacion == "Iniciar Sesión":
    usuario = iniciar_sesion(usuarios)
    if usuario:
        if usuario:
            st.session_state.usuario = usuario  # Guardar el usuario en la sesión
        # Botón para ir a la nueva página
        if st.button("Ir a la nueva página"):
            mostrar_pagina_busqueda()

elif opcion_autenticacion == "Registrarse":
    crear_usuario(usuarios)

# Sección de cambio de contraseña

if opcion_autenticacion == "Cambiar Contraseña":
    st.header("Cambiar Contraseña")

    # Variable de estado para controlar si se ha presionado el botón de cambiar contraseña
    cambiar_contraseña_pressed = st.session_state.get("cambiar_contraseña_pressed", False)

    # Mostrar el botón de cambiar contraseña
    if not cambiar_contraseña_pressed:
        if st.button("Cambiar Contraseña"):
            # Actualizar la variable de estado para indicar que se ha presionado el botón
            st.session_state.cambiar_contraseña_pressed = True
    else:
        # Si se ha presionado el botón de cambiar contraseña, mostrar los campos de contraseña actual y nueva
        if st.session_state.usuario:
            contraseña_actual = st.text_input("Contraseña Actual", type="password")
            nueva_contraseña = st.text_input("Nueva Contraseña", type="password")

            if st.selectbox("¿Desea cambiar la contraseña?", ("No", "Sí")) == "Sí" and st.button("Cambiar Contraseña"):
                cambiar_contraseña(st.session_state.usuario, nueva_contraseña)
        else:
            st.write("Por favor, inicia sesión para cambiar la contraseña.")
else:
    st.write("Selecciona la opción 'Cambiar Contraseña' para cambiar tu contraseña.")


# Seccion buscar lugares Colombia
st.header("Buscar Lugares en Colombia")
ciudad = st.text_input("Ingrese el nombre de una ciudad colombiana:")
if ciudad:
    lugares = buscar_lugares_ciudad(ciudad)
    st.write(f"Lugares bonitos e importantes de {ciudad.capitalize()}:")
    for lugar in lugares:
        st.write(f"- {lugar}")


# Seccion buscar lugares paises América
st.header("Buscar Lugares en América")
if st.session_state.usuario:
   paises = ["Argentina", "Brasil", "Canadá", "Chile", "Costa Rica", "Cuba", "Estados Unidos", "México", "Panamá", "Paraguay", "Perú", "Puerto Rico", "Uruguay", "Venezuela"]
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



# Sección "Acerca de mí"
st.header("Acerca de Mí")
st.write('''Mi nombre es Santiago Molina Velasquez y soy estudiante 
             de ingeniería de sistemas en la Universidad Nacional de Colombia. 
             Me apasiona el mundo de la tecnología y estoy comprometido a brindar soluciones 
             innovadoras a través del desarrollo de software y la ingeniería de sistemas. 
             Tengo como metas cercanas terminar mi carrera profesional y seguir 
             consolidándome y laborando en todo lo relacionado a tecnología y 
             en el gran mundo del internet.''')
st.write("Puedes contactarme en smolinav@unal.edu.co")

# Sección "Tratamiento de Datos"
st.header("Tratamiento de Datos")
st.write('''Tratamiento de Datos en nuestra Nueva Aplicación de Viajes

En nuestra emocionante nueva aplicación de viajes, nos esforzamos por brindar una experiencia 
         personalizada y sobresaliente para cada uno de nuestros valiosos usuarios. 
         Para lograr esto, recopilamos datos de inicio de sesión con el único propósito 
         de mejorar nuestras recomendaciones de destinos de viaje y proporcionar 
         respuestas más precisas a tus consultas.

Es importante destacar que los datos que recopilamos nunca abandonarán nuestra aplicación. 
         No los vendemos ni compartimos con terceros para ningún propósito, 
         incluidos fines publicitarios. 
         Tu privacidad y seguridad son nuestras principales prioridades.

Entendemos que el tiempo es valioso, por lo que hemos establecido un período de retención
          de datos de un año como máximo. Si durante este tiempo no actualizas tu perfil o 
         utilizas la aplicación, tus datos se eliminarán automáticamente para garantizar 
         que solo conservemos la información relevante y actualizada.

Nos comprometemos a ser transparentes en nuestras prácticas de privacidad y seguridad. 
         Si tienes alguna pregunta o inquietud sobre cómo manejamos tus datos, 
         no dudes en ponerte en contacto con nuestro equipo de soporte, 
         siempre estaremos encantados de ayudarte.

Gracias por confiar en nosotros para planificar tus aventuras. 
         ¡Esperamos que disfrutes explorando el mundo con nuestra aplicación!
         ''')

