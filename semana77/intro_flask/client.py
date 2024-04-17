import requests

url = 'http://localhost:5000/'
response = requests.get(url)
print(response.text)

# para nuestro metodo get nombre
params = {'nombre': 'Betzabe'}
response = requests.get(url + 'saludar', params=params)
print(response.text)
#suma
num1 = 12
num2 = 6
url = f"{url}/sumar?num1={num1}&num2={num2}"
response = requests.get(url)
print(response.text)

# palindromo
cadena = "reconocer"
url = f"{url}/palindromo?cadena={cadena}"
response = requests.get(url)
print(response.text)