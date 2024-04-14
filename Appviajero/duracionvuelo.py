import numpy as np

def calcular_duracion_vuelo(distancia_km, velocidad_promedio_kmh):
    # Convertir la distancia a millas náuticas (1 km = 0.539957 millas náuticas)
    distancia_nm = distancia_km * 0.539957
    
    # Calcular la duración del vuelo en horas
    duracion_horas = distancia_nm / velocidad_promedio_kmh
    
    return duracion_horas

