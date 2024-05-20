# Importar las librerías necesarias
import streamlit as st # type: ignore
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial.distance import cdist

import geopandas as gpd
import plotly.express as px
import plotly.graph_objs as go

# Guardar en la variable 'ruta' la url del dataset
# Cities
ruta = 'https://raw.githubusercontent.com/SMOLINAV/ppi_dai_MOLINAs/\
main/Appviajero/datos/World_Airports.csv'

# Cargar el dataset a partir de la ruta establecida
datos = gpd.read_file(ruta)

# Convertir las columnas 'latitude_deg' y 'longitude_deg'
datos['latitude_deg'] = pd.to_numeric(datos['latitude_deg'])
datos['longitude_deg'] = pd.to_numeric(datos['longitude_deg'])

# Graficar el mapa
def graficar_mapa(df):
    fig = px.scatter_mapbox(df,
                            lat="latitude_deg",
                            lon="longitude_deg",
                            hover_name="name",
                            hover_data={"iso_country": True},
                            zoom=10,
                            height=600)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(title="Mapa de aeropuertos")

    return fig

# Buscar aeropuertos por iso_paises
def buscar_aeropuertos_por_pais(df, codigo_pais):
    resultados = df[df['iso_country'] == codigo_pais]
    return resultados
