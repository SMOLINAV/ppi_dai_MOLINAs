import numpy as np

def calcular_distancia_entre_puntos(coord1, coord2):
    """
    Calcula la distancia euclidiana entre dos puntos en un espacio bidimensional.

    Args:
        coord1 (tuple): Coordenadas del primer punto (x, y).
        coord2 (tuple): Coordenadas del segundo punto (x, y).

    Returns:
        float: Distancia euclidiana entre los dos puntos.
    """
    x1, y1 = coord1
    x2, y2 = coord2
    distancia = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def calcular_distancia_total(coordenadas):
    """
    Calcula la distancia total recorrida en una ruta de viaje representada por una lista de coordenadas.

    Args:
        coordenadas (list): Lista de coordenadas de los puntos en la ruta de viaje.

    Returns:
        float: Distancia total recorrida en la ruta de viaje.
    """
    distancia_total = 0
    for i in range(len(coordenadas) - 1):
        distancia_total += calcular_distancia_entre_puntos(coordenadas[i], coordenadas[i+1])
    # Agrega la distancia desde el último punto de regreso al punto de inicio
    distancia_total += calcular_distancia_entre_puntos(coordenadas[-1], coordenadas[0])
    return distancia_total

# Ejemplo de uso
if __name__ == "__main__":
    coordenadas_ejemplo = [(0, 0), (3, 4), (6, 8), (9, 6)]
    distancia_total = calcular_distancia_total(coordenadas_ejemplo)
    print("Distancia total recorrida:", distancia_total)