# Debe buscar las ciudades del pais que se le ingrese
def buscar_lugares_ciudad_pais(pais):
    if pais.lower() == "argentina":
        return {
            "Buenos Aires": ["Casa Rosada", "Recoleta", "Caminito"],
            "Córdoba": ["Manzana Jesuítica", "Cerro Uritorco", "Río de los Sauces"],
            "Bariloche": ["Cerro Catedral", "Circuito Chico", "Cerro Campanario"]
        }
    elif pais.lower() == "brasil":
        return {
            "Río de Janeiro": ["Cristo Redentor", "Pan de Azúcar", "Copacabana"],
            "São Paulo": ["Avenida Paulista", "Parque Ibirapuera", "Mercado Municipal"],
            "Salvador": ["Pelourinho", "Playa Porto da Barra", "Farol da Barra"]
        }
    elif pais.lower() == "méxico":
        return {
            "Ciudad de México": ["Zócalo", "Museo Frida Kahlo", "Xochimilco"],
            "Cancún": ["Zona Hotelera", "Parque Xcaret", "Playa Delfines"],
            "Guadalajara": ["Hospicio Cabañas", "Catedral de Guadalajara", "Tlaquepaque"]
        }
    # Agrega más países y ciudades aquí...
    else:
        return {}
    
    