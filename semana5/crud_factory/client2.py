import requests
import json

url = "http://localhost:8000/deliveries"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_chocolate_data = {
    "chocolate_type": "tableta",
    "peso": 50,
    "sabor": "Dulce"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "tableta",
    "peso": 24,
    "sabor": "Dulce"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())


# GET /deliveries
response = requests.get(url=url)
print(response.json())

# PUT /deliveries/{chocolate_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "peso": 12
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

# DELETE /deliveries/{vehicle_id}
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())