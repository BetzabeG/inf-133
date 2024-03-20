import requests

url = 'http://localhost:8000'

# Listar todos los posts
def listar_posts():
    response = requests.get(f'{url}/posts')
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error al listar los posts'

# Obtener el post 2
def obtener_post(post_id):
    response = requests.get(f'{url}/post/{post_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error al obtener el post'

# Crear un nuevo post
def crear_post(titulo, contenido):
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    data = {'title': titulo, 'content': contenido}
    response = requests.post(f'{url}/posts', data=data, headers=headers)
    if response.status_code == 201:
        return response.json()
    else:
        return 'Error al crear el post'

# Actualizar el contenido del post 3
def actualizar_post(post_id, nuevo_contenido):
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    data = {'content': nuevo_contenido}
    response = requests.put(f'{url}/post/{post_id}', data=data, headers=headers)
    if response.status_code == 200:
        return 'Post actualizado correctamente'
    else:
        return 'Error al actualizar el post'

# Eliminar el post 2
def eliminar_post(post_id):
    response = requests.delete(f'{url}/post/{post_id}')
    if response.status_code == 200:
        return 'Post eliminado correctamente'
    else:
        return 'Error al eliminar el post'

# Ejemplo
print(listar_posts())
print(obtener_post(2))
print(crear_post('Mi experiencia como dev', 'Aquí describirías tu experiencia como desarrollador.'))
print(actualizar_post(3, 'En progreso'))
print(eliminar_post(2))
