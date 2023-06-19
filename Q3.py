import folium
import requests
import time

# Clé API
api_key = 'e0a1bf2c844edb9084efc764c089dd748676cc14'

contract_name = 'Paris'


# URL de l'API
url = f'https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}'


# Création de la carte
map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)  # Coordonnées de Paris

def update_map():
    # Envoi de la requête GET à l'API
    response = requests.get(url)

    # Vérification du statut de la réponse
    if response.status_code == 200:
        data = response.json()  # Conversion de la réponse en format JSON

        # Suppression des anciens marqueurs
        map.get_root().html.add_child(folium.Element('<script>document.getElementsByClassName("marker-cluster").forEach(function(item) { item.remove(); });</script>'))

        # Ajout des nouveaux marqueurs pour chaque station
        for station in data:
            name = station['name']
            lat = station['position']['lat']
            lon = station['position']['lng']
            available_bikes = station['available_bikes']
            total_bikes = station['bike_stands']

            # Création du marqueur
            marker = folium.Marker(
                location=[lat, lon],
                popup=f"Station: {name}<br>Available bikes: {available_bikes}/{total_bikes}"
            )
            marker.add_to(map)

        print("Les données ont été mises à jour.")

    else:
        print("Erreur lors de la requête à l'API :", response.status_code)

# Actualisation des données toutes les minutes
while True:
    update_map()
    time.sleep(60)  # Attente de 60 secondes

