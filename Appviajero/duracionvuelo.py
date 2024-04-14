import numpy as np

def calcular_duracion_vuelo(distancia_km, velocidad_promedio_kmh):
    # Convertir la distancia a millas náuticas (1 km = 0.539957 millas náuticas)
    distancia_nm = distancia_km * 0.539957
    
    # Calcular la duración del vuelo en horas
    duracion_horas = distancia_nm / velocidad_promedio_kmh
    
    return duracion_horas

# Calculo de la duración del vuelo
distancia_km = float(input("Ingrese la distancia entre los dos puntos en kilómetros: "))
velocidad_promedio_kmh = 800  # Velocidad promedio de un avión

duracion_vuelo = calcular_duracion_vuelo(distancia_km, velocidad_promedio_kmh)
print("Duración del vuelo:", duracion_vuelo, "horas")
