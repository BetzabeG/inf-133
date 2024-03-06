import requests
# Definir la consulta GraphQL
query = """
    {
        estudiantes {
            id
            nombre
            apellido
            carrera          
        }
    }
"""
# Realiza la consulta desde el cliente para que solo devuelva el nombre
query = """
    {
        estudiantes {
            nombre         
        }
    }
"""

# Realiza la consulta desde el cliente para que solo devuelva el nombre y apellido
query = """
    {
        estudiantes {
            nombre
            apellido         
        }
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)