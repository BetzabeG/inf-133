import requests
#Definir a consulta GraphQL
query = """
    {
        hello
        goodbye    
    }
"""
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GrapQL
response = requests.post(url, json={'query': query})
print(response.text)