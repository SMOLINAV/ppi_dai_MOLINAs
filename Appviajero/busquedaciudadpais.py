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
    elif pais.lower() == "canadá":
        return {
            "Toronto": ["CN Tower", "Casa Loma", "Distillery District"],
            "Montreal": ["Mont Royal", "Vieux-Montréal", "Basílica de Notre-Dame"],
            "Vancouver": ["Parque Stanley", "Granville Island", "Puente Colgante Capilano"]
        }
    elif pais.lower() == "cuba":
        return {
            "La Habana": ["La Habana Vieja", "Malecón", "Plaza de la Revolución"],
            "Trinidad": ["Plaza Mayor", "Valle de los Ingenios", "Playa Ancón"],
            "Varadero": ["Playa Varadero", "Parque Josone", "Cueva de Ambrosio"]
        }
    elif pais.lower() == "venezuela":
        return {
            "Caracas": ["Panteón Nacional", "Ávila", "Plaza Bolívar"],
            "Mérida": ["Teleférico de Mérida", "Pico Bolívar", "Plaza Bolívar"],
            "Isla Margarita": ["Playa El Agua", "Parque Nacional Laguna de la Restinga", "Fortín de la Galera"]
        }
    elif pais.lower() == "perú":
        return {
            "Lima": ["Plaza Mayor", "Barrio de Miraflores", "Barrio de Barranco"],
            "Cusco": ["Machu Picchu", "Plaza de Armas", "Valle Sagrado"],
            "Arequipa": ["Plaza de Armas", "Monasterio de Santa Catalina", "Cañón del Colca"]
        }
    elif pais.lower() == "estados unidos":
        return {
            "Nueva York": ["Times Square", "Central Park", "Estátua de la Libertad"],
            "Los Ángeles": ["Hollywood", "Santa Mónica Pier", "Universal Studios Hollywood"],
            "San Francisco": ["Puente Golden Gate", "Alcatraz", "Fisherman's Wharf"]
        }
    elif pais.lower() == "costa rica":
        return {
            "San José": ["Museo Nacional de Costa Rica", "Teatro Nacional de Costa Rica", "Parque Metropolitano La Sabana"],
            "Monteverde": ["Reserva Biológica Bosque Nuboso Monteverde", "Serpentario Monteverde", "Santuario Ecológico"],
            "Manuel Antonio": ["Parque Nacional Manuel Antonio", "Playa Manuel Antonio", "Isla Damas"]
        }
    elif pais.lower() == "puerto rico":
        return {
            "San Juan": ["Viejo San Juan", "Fuerte San Felipe del Morro", "El Yunque"],
            "Ponce": ["Plaza las Delicias", "Catedral de Nuestra Señora de Guadalupe", "Museo de Arte de Ponce"],
            "Rincón": ["Playa Domes", "Faros de Rincón", "Mirador de Rincón"]
        }
    elif pais.lower() == "panamá":
        return {
            "Ciudad de Panamá": ["Casco Viejo", "Canal de Panamá", "Mercado de Mariscos"],
            "Bocas del Toro": ["Isla Colón", "Playa Estrella", "Cayo Zapatilla"],
            "Boquete": ["Volcán Barú", "Sendero de los Quetzales", "Los Cangilones de Gualaca"]
        }
    elif pais.lower() == "chile":
        return {
            "Santiago": ["Plaza de Armas", "Cerro San Cristóbal", "Barrio Bellavista"],
            "Valparaíso": ["Cerro Concepción", "Ascensor Artillería", "La Sebastiana"],
            "San Pedro de Atacama": ["Valle de la Luna", "Salar de Atacama", "Laguna Cejar"]
        }
    elif pais.lower() == "paraguay":
        return {
            "Asunción": ["Plaza de los Héroes", "Costanera de Asunción", "Panteón de los Héroes"],
            "Encarnación": ["Costanera de Encarnación", "Santuario del Ñandutí", "Ruinas Jesuíticas de Jesús y Trinidad"],
            "Ciudad del Este": ["Represa de Itaipú", "Mercado de Ciudad del Este", "Shopping Paris"]
        }
    elif pais.lower() == "uruguay":
        return {
            "Montevideo": ["Ciudad Vieja", "Rambla de Montevideo", "Mercado del Puerto"],
            "Punta del Este": ["La Mano en la Arena", "Puerto de Punta del Este", "Casapueblo"],
            "Colonia del Sacramento": ["Barrio Histórico de Colonia del Sacramento", "Faro de Colonia del Sacramento", "Plaza Mayor 25 de Mayo"]
        }
    else:
        return {}
