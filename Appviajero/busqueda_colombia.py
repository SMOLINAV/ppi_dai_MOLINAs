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
    elif ciudad.lower() == "cúcuta":
        return ["Parque Nacional Natural Los Estoraques", "Museo del Agua", "Catedral de San José", "Mirador Cristo Rey"]
    elif ciudad.lower() == "manizales":
        return ["Nevado del Ruiz", "Catedral Basílica Metropolitana de Manizales", "Cable Aéreo de Manizales", "Parque Natural Regional Río Blanco"]
    elif ciudad.lower() == "pasto":
        return ["Volcán Galeras", "Plaza de Nariño", "Laguna de la Cocha", "Iglesia de San Felipe"]
    elif ciudad.lower() == "valledupar":
        return ["Parque de la Leyenda Vallenata", "Museo del Acordeón", "Cerro de la Popa", "Catedral de Santa Bárbara de Valledupar"]
    elif ciudad.lower() == "ibagué":
        return ["Nevado del Tolima", "Jardín Botánico San Jorge", "Catedral Primada de Ibagué", "Lago del Totumo"]
    elif ciudad.lower() == "villavicencio":
        return ["Parque Los Ocarros", "Bioparque Makuira", "Catedral Nuestra Señora del Carmen", "Mirador El Calvario"]
    elif ciudad.lower() == "montería":
        return ["Parque Nacional Natural Paramillo", "Catedral San Jerónimo de Montería", "Parque Ronda del Sinú", "Plaza Cultural de la Castellana"]
    elif ciudad.lower() == "manizales":
        return ["Nevado del Ruiz", "Catedral Basílica Metropolitana de Manizales", "Cable Aéreo de Manizales", "Parque Natural Regional Río Blanco"]
    elif ciudad.lower() == "sogamoso":
        return ["Laguna de Tota", "Catedral Basílica del Milagroso Señor de los Milagros", "Monumento a la Virgen del Milagro", "Parque Arqueológico de Monquirá"]
    else:
        return ["Lo sentimos, no encontramos información para esta ciudad."]