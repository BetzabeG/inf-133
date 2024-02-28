import requests

card_number = "BT1-010"

url = f"https://digimoncard.io/api-public/search.php?card={card_number}"

response = requests.request(
    method="GET", 
    url=url, 
    headers={"Content-Type": "application/json"}, 
    data={}
)
print(response.text)

#sevicios rest necesitan un metodo
#metodo y forma de acceder al servicio (DIFERENCIA ENTRE SOAP Y REST)
#1- METODO DE CONSULTA
#2. LA FORMA EN QUE SE ACCEDE AL SERVICIO

#SOAP--> es un protocolo
#REST-->es una arquitectura se comunica con json