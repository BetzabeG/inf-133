from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "Hola, {}!".format(nombre)

def SumaDosNumeros(num1, num2):
    return num1 + num2

def CadenaPalindromo(cadena):
    return cadena == cadena[::-1]

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str}
)

dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"resultado": int},
    args={"num1": int, "num2": int}
)

dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns={"es_palindromo": bool},
    args={"cadena": str}
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatchers
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()