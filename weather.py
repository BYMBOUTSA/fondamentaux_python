import requests

# Récupérer notre clef API
with open('api_key.txt', 'r') as f:
    api_key = f.read()

# Obtenir la météo pour qu'elle ville ?
city_name = input('Pour quelle ville souhaites-tu obtenir la météo ? ')

# Construction de la requête.
api_request = f'https://api.openweathermap.org/data/2.5/weather?q={city_name.lower()}&appid={api_key}&lang=fr&units=metric'

result = requests.get(api_request)


if result.status_code == 200:
    # Convertir le résultat au format JSON
    result = result.json()

    # Récupérer la météo globale
    weather = result['weather']

    print(f'Météo à {city_name}')
    for element in weather:
        print(f'- {element["description"]}')

    # Récupérer la température
    print(f'Temperature: {result["main"]["temp"]}')

else:
    print(f'ERROR: status_code {result.status_code}')

