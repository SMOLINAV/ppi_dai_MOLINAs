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
    elif ciudad.lower() == "sogamoso":
        return ["Laguna de Tota", "Catedral Basílica del Milagroso Señor de los Milagros", "Monumento a la Virgen del Milagro", "Parque Arqueológico de Monquirá"]
    elif ciudad.lower() == "arauca":
        return ["Parque Nacional Natural El Tuparro", "Puente José Antonio Páez", "Catedral de San Bartolomé", "Plaza Bolívar de Arauca"]
    elif ciudad.lower() == "quibdó":
        return ["Reserva Natural Serranía del Baudó", "Catedral de San Francisco de Asís", "Malecón de Quibdó", "Plaza Cívica José María Cordoba"]
    elif ciudad.lower() == "riohacha":
        return ["Desierto de la Guajira", "Catedral Nuestra Señora de los Remedios", "Parque de la Marina", "Plaza José Prudencio Padilla"]
    elif ciudad.lower() == "quindío":
        return ["Parque Nacional Natural Los Nevados", "Parque del Café", "Jardín Botánico del Quindío", "Viaducto César Gaviria Trujillo"]
    elif ciudad.lower() == "yopal":
        return ["Reserva Natural Laguna de la Leche", "Catedral Santiago de los Caballeros", "Puente Real de Boyacá", "Monumento a la Libertad de Yopal"]
    elif ciudad.lower() == "leticia":
        return ["Reserva Natural Marasha", "Parque Nacional Natural Amacayacu", "Catedral Nuestra Señora de la Paz", "Malecón Turístico"]
    elif ciudad.lower() == "flores":
        return ["Laguna de Yarinacocha", "Catedral Nuestra Señora de la Asunción", "Mercado de Belén", "Plaza Mayor"]
    elif ciudad.lower() == "mitú":
        return ["Reserva Nacional Natural Puinawai", "Catedral de San José", "Parque Japonés", "Plaza de la Paz"]
    elif ciudad.lower() == "trinidad":
        return ["Iglesia de la Santísima Trinidad", "Parque Nacional Madidi", "Museo de Historia Natural Noel Kempff Mercado", "Malecón de la Costanera"]
    elif ciudad.lower() == "sacaba":
        return ["Iglesia de San Pedro", "Parque Nacional Tunari", "Casa de la Cultura de Sacaba", "Jardín Botánico La Boliviana"]
    elif ciudad.lower() == "cobija":
        return ["Catedral de Cobija", "Plaza 10 de Febrero", "Parque Nacional Madidi", "Iglesia de San Pedro"]
    elif ciudad.lower() == "sucre":
        return ["Catedral de Nuestra Señora de Guadalupe", "Plaza 25 de Mayo", "Parque Cretácico", "Iglesia de San Lázaro"]
    elif ciudad.lower() == "oruro":
        return ["Carnaval de Oruro", "Catedral Basílica Menor de San Felipe", "Museo Nacional Antropológico", "Mirador del Cerro Santa Bárbara"]
    elif ciudad.lower() == "tarija":
        return ["Catedral San Bernardo", "Plaza Luis de Fuentes", "Museo Paleontológico y Arqueológico", "Parque Temático Megalítico"]
    elif ciudad.lower() == "cisneros":
        return ["Iglesia de Nuestra Señora de las Mercedes", "Cerro El Capiro", "Parque Recreacional Capiro y Campana", "Mirador de la Virgen"]
    elif ciudad.lower() == "rionegro":
        return ["Parque Principal Santander", "Iglesia de Nuestra Señora del Rosario", "Cascada La Romera", "Laguna El Tablazo"]
    elif ciudad.lower() == "guatapé":
        return ["Piedra del Peñol", "Represa de Guatapé", "Malecón de Guatapé", "Iglesia de Nuestra Señora del Carmen"]
    elif ciudad.lower() == "marinilla":
        return ["Parque Principal de Marinilla", "Iglesia de San José", "Mirador de la Cruz", "Cascada La Chorrera"]
    elif ciudad.lower() == "guarne":
        return ["Parque Principal de Guarne", "Iglesia de San Juan Bautista", "Cerro Quitasol", "Cascada La Miel"]
    elif ciudad.lower() == "sopetrán":
        return ["Parque Principal de Sopetrán", "Iglesia de Nuestra Señora de las Mercedes", "Cascada El Salado", "Cerro El Picacho"]
    elif ciudad.lower() == "santa fe":
        return ["Cascada La Mina", "Mirador de Santa Fe", "Plaza Principal de Santa Fe", "Iglesia de Santa Bárbara"]
    elif ciudad.lower() == "armenia":
        return ["Jardín Botánico del Quindío", "Parque de la Vida", "Café Park", "Iglesia de San Francisco de Asís"]
    else:
        return ["Lo sentimos, no encontramos información para esta ciudad."]