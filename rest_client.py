import requests

url = "http://localhost:8000/"
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

# GET a la ruta /buscar_nombre
ruta_buscar = url + "buscar_nombre"
buscar_response = requests.get(ruta_buscar)
print(buscar_response.text)

# GET a la ruta /contar_carreras
ruta_contar = url + "contar_carreras"
contar_response = requests.get(ruta_contar)
print(contar_response.text)

# GET a la ruta /total_estudiantes  
ruta_total = url + "total_estudiantes"
total_response = requests.get(ruta_total)
print(total_response.text)

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)
print(post_response.text)