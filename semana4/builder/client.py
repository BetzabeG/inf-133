import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

pizza = {
    "tamaño": "Mediana",
    "masa": "Gruesa",
    "toppings": ["Jamon", "Queso", "Tomate"]
}
response = requests.post(url, json=pizza, headers=headers)
print(response.json())