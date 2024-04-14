# busqueda_colombia.py

def buscar_lugares_ciudad(ciudad):
    """
    Esta función busca y devuelve una lista de lugares bonitos e importantes de la ciudad especificada en Colombia.
    
    Args:
        ciudad (str): El nombre de la ciudad colombiana.
    
    Returns:
        list: Una lista de lugares bonitos e importantes de la ciudad.
    """
    # Aquí puedes implementar la lógica para buscar los lugares de la ciudad en Colombia
    # Por ahora, simplemente devolvemos una lista de lugares de ejemplo
    if ciudad.lower() == "bogota":
        return ["Monserrate", "Plaza de Bolívar", "Museo del Oro", "La Candelaria"]
    elif ciudad.lower() == "medellin":
        return ["Parque Arví", "Plaza Botero", "Parque Explora", "Comuna 13"]
    elif ciudad.lower() == "cartagena":
        return ["Ciudad Amurallada", "Castillo de San Felipe", "Playa Blanca", "Islas del Rosario"]
    else:
        return ["Lo sentimos, no encontramos información para esta ciudad."]

