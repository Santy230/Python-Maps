from os import system
import googlemaps
from geopy import Nominatim

API_KEY = "*****"
gmaps = googlemaps.Client(key=API_KEY)

def obtener_coordenadas(): #COORDENADAS APROXIMADAS DE LA DIRRECION INGRESADA
    try:
        geolocator = Nominatim(user_agent="Deciciones")
        direccion = input("Ingrese Direccion " + "En Argentina ")
        provincia = input("Ingrese Provincia ")
        Localidad = input("Ingrese Localidad ")
        location = geolocator.geocode(direccion +"," +provincia+"," +","+ Localidad)
        return location.latitude,location.longitude
    except:
        print("Direccion No ENCONTRADA")
def imprimir_results(place_details):    #MUESTRA LOS LUGARES
    try:
        print(f"Lugar: {place_details['result']['name']},"
            f" Clasificacion: {place_details['result']['rating']}"
            f" Numero: {place_details['result']['formatted_phone_number']}")

    except:
        pass

def lugares_cerca():    #CONSIGUE LOS LUGARES CERCA Y LOS GUARDA EN UNA VARIABLE
    results = gmaps.places_nearby(location= obtener_coordenadas()
                                 ,radius = 2000
                                  ,open_now = False
                                  ,type = 'restaurant',)
    for places in results['results']:
        my_places_id = places['place_id']
        my_fields: list[str] = ['name','rating','formatted_phone_number']
        place_details = gmaps.place(place_id = my_places_id,fields = my_fields)
        imprimir_results(place_details)
    system('pause')
