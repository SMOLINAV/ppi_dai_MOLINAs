import streamlit as st
from auth import cargar_usuarios, crear_usuario, iniciar_sesion
from nueva_pestana import mostrar_pagina_busqueda

# Cargar usuarios al iniciar la aplicación
usuarios = cargar_usuarios()

# Título de la aplicación
st.title("APP VIAJEROFELIZ - Planificador de Viajes")

# Sección de "Iniciar Sesión" o "Registrarse"
st.header("Autenticación")
opcion_autenticacion = st.radio("Selecciona una opción:", ("Iniciar Sesión", "Registrarse"))

if opcion_autenticacion == "Iniciar Sesión":
    usuario = iniciar_sesion(usuarios)
    if usuario:
        # Botón para ir a la nueva página
        if st.button("Ir a la nueva página"):
            mostrar_pagina_busqueda()

elif opcion_autenticacion == "Registrarse":
    crear_usuario(usuarios)

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
st.write("Aquí puedes realizar análisis y tratamiento de datos según tus necesidades.")
# Agrega aquí la funcionalidad de tratamiento de datos según lo que se necesite
