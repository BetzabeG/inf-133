from zeep import Client
client = Client('http://localhost:8000')

result = client.service.Saludar(nombre="Betzabe")
print(result)
num1=10
num2=14
suma = client.service.SumaDosNumeros(num1=num1,num2=num2)
print(f"La suma de {num1} y {num2} es: {suma}",)

cadena = "radar"
resultado_palindromo = client.service.CadenaPalindromo(cadena=cadena)
print(f"{cadena} es palindromo ? {resultado_palindromo}")

