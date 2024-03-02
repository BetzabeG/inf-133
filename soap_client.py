from zeep import Client
client = Client('http://localhost:8000')

result = client.service.Saludar(nombre="Betzabe")
print(result)

suma = client.service.SumaDosNumeros(num1=10,num2=14)
print(suma)

cadena = "radar"
resultado_palindromo = client.service.CadenaPalindromo(cadena=cadena)
print(cadena, resultado_palindromo)

#Entrega por GIT HUB enlace repositorio a GitHub