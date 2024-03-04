import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)


# Agregar dos estudiantes de Economía
nuevo_estudiante1 = {
    "nombre": "María",
    "apellido": "López",
    "carrera": "Economía",
}

nuevo_estudiante2 = {
    "nombre": "Juan",
    "apellido": "Martínez",
    "carrera": "Economía",
}

response_post1 = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante1)
response_post2 = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante2)

print("Estudiante 1 agregado :", response_post1.text)
print("Estudiante 2 agregado:", response_post2.text)



# DELETE elimina todos los estudiantes por la ruta /estudiantes
ruta_eliminar = url + "estudiantes"
eliminar_response = requests.request(method="DELETE", 
                                    url=ruta_eliminar)
print(eliminar_response.text)



post_response = requests.request(method="POST", 
                        url=ruta_post,
                        json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingeniería",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# GET busca a un estudiante por id /estudiantes/{id}
ruta_filtrar_nombre = url + "estudiantes/1"
filtrar_nombre_response = requests.request(method="GET", 
                                url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)

#GET mostrar todas las carreras ********
mostrar_carrera = url + "carreras"
mostrar= requests.request(method="GET", 
                url=mostrar_carrera)
print("Todas las carreras")
print(mostrar.text)

#GET Devuelva a todos los estudiantes de la carrera de Economia
devuelve_carrera_economia = url + "estudiantes_economia"
devuelve= requests.request(method="GET", 
                url=devuelve_carrera_economia)
print("Estudiantes de economia")
print(devuelve.text)


# PUT actualiza un estudiante por la ruta /estudiantes
ruta_actualizar = url + "estudiantes"
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=estudiante_actualizado
)
print(put_response.text)