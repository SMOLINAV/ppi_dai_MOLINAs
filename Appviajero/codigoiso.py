import streamlit as st # type: ignore
import pandas as pd

def extraer_codigo_iso(pais):
    '''
    Esta función extrae el código ISO 3166-1 alfa-2 de un país dado por el usuario.
    args:
        pais (str): nombre del país
    returns:
        codigo_iso (str): código ISO 3166-1 alfa-2 del país
        None (None): si no se encuentra el código ISO
    '''
    # URL de la página que contiene la lista de códigos ISO 3166-1
    url = "https://es.wikipedia.org/wiki/ISO_3166-1"

    # Leer las tablas de la página
    try:
        tablas = pd.read_html(url)
    except ImportError as e:
        st.error("Necesitas instalar la biblioteca lxml. Usa `pip install lxml`.")
        return None

    # Intentar encontrar la tabla correcta
    iso_table = None
    for tabla in tablas:
        if 'Nombre común' in tabla.columns:
            iso_table = tabla
            break

    # Si no se encuentra la tabla, devolver None
    if iso_table is None:
        return None

    # Renombramos las columnas basándonos en la estructura esperada
    iso_table = iso_table[['Nombre común', 'Código alfa-2', 'Código alfa-3', 'Código numérico']]

    # Buscar el país en la columna 'Nombre común'
    for fila in iso_table.itertuples(index=False):
        if str(pais).lower() in str(fila[0]).lower():
            return fila[1].strip()

    # Si no se encontró el país, devolver None
    return None

# Ejemplo de uso en la aplicación Streamlit
st.title("Buscar Código ISO de un País")
nombrecomun = st.text_input("Ingrese el nombre del país:")
if st.button("Ver Código ISO"):
    codigonombre = extraer_codigo_iso(nombrecomun)
    if codigonombre:
        st.write(f"El código ISO alfa-2 de {nombrecomun} es: {codigonombre}")
    else:
        st.write(f"No se encontró el código ISO alfa-2 para {nombrecomun}.")
