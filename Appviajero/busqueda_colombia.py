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
    if ciudad.lower() == "bogotá":
        return ["Monserrate", "Plaza de Bolívar", "Museo del Oro", "La Candelaria"]
    elif ciudad.lower() == "medellín":
        return ["Parque Arví", "Plaza Botero", "Parque Explora", "Comuna 13"]
    elif ciudad.lower() == "cartagena":
        return ["Ciudad Amurallada", "Castillo de San Felipe", "Playa Blanca", "Islas del Rosario"]
    elif ciudad.lower() == "cali":
        return ["Cristo Rey", "Zoológico de Cali", "Cerro de las Tres Cruces", "Iglesia La Ermita"]
    elif ciudad.lower() == "santa marta":
        return ["Parque Nacional Natural Tayrona", "Playa El Rodadero", "Quinta de San Pedro Alejandrino", "Sierra Nevada de Santa Marta"]
    elif ciudad.lower() == "pereira":
        return ["Parque Consotá", "Bioparque Ukumarí", "Catedral de Nuestra Señora de la Pobreza", "Laguna del Otún"]
    elif ciudad.lower() == "bucaramanga":
        return ["Parque Nacional del Chicamocha", "Parque del Agua", "Catedral de la Sagrada Familia", "Cascada de Juan Curi"]
    elif ciudad.lower() == "barranquilla":
        return ["Malecón Puerta de Oro", "Museo del Caribe", "Castillo de Salgar", "Plaza de San Nicolás"]
    else:
        return ["Lo sentimos, no encontramos información para esta ciudad."]