import requests

# Clé API
api_key = 'e0a1bf2c844edb9084efc764c089dd748676cc14'

#name
contract_name = 'Paris'


# URL de l'API
url = f'https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}'



# Envoi de la requête GET à l'API
response = requests.get(url)

# Vérification du statut de la réponse
if response.status_code == 200:
    data = response.json()  # la réponse en format JSON
    

    # Pourcentage de vélos mécaniques vs électriques
    total_bikes = len(data)
    mechanical_bikes = sum(1 for station in data if station['banking'])
    electric_bikes = total_bikes - mechanical_bikes
    mechanical_bikes_percentage = (mechanical_bikes / total_bikes) * 100
    electric_bikes_percentage = (electric_bikes / total_bikes) * 100
    print(f"Pourcentage de vélos mécaniques : {mechanical_bikes_percentage:.2f}%")
    print(f"Pourcentage de vélos électriques : {electric_bikes_percentage:.2f}%")

    # Classement des villes avec le plus de vélos
    cities = {}
    for station in data:
        city = station['contract_name']
        if city in cities:
            cities[city] += 1
        else:
            cities[city] = 1
    sorted_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)
    print("Classement des villes avec le plus de vélos :")
    for city, count in sorted_cities:
        print(f"{city} : {count}")

else:
    print("Erreur lors de la requête à l'API :", response.status_code)
