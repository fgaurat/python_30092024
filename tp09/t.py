import requests

# URL de l'API
url = "https://api.data.gouv.fr/v1/datasets/valeurs-foncieres/"

# Paramètres de la requête (ajustez selon vos besoins)
params = {
    "q": "Paris",  # Exemple : "Paris"
    "limit": 10,  # Limite le nombre de résultats
    "offset": 0   # Pour paginer les résultats
}

# Faire la requête GET
response = requests.get(url, params=params)

# Vérifier le statut de la réponse
if response.status_code == 200:
    # Convertir la réponse en JSON
    data = response.json()
    # Traiter les données (ici, nous les affichons)
    print(data)
else:
    print(f"Erreur lors de la requête : {response.status_code}")