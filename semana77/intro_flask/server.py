from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, mundo!'
#agregamos a una nueva ruta
@app.route('/saludar', methods = ['GET'])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parametros de la URL "}),
            400,
        )
    return jsonify({"mensaje": f"Hola, {nombre}!"})

# Agregamos una ruta para Suma dos numeros

@app.route('/sumar', methods = ['GET'])
def sumar():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    suma = int(num1) + int(num2)
    if not int(num1) and not int(num2):
        return(
            jsonify({"error": "Se requiere un nombre en los parametros de la URL"}),400
        )
    return jsonify({"mensaje": f"{suma}"})

# agregamos ruta para palilndromo
@app.route('/palindromo', methods = ['GET'])
def palindromo():
    cadena = request.args.get("cadena")
    if not cadena:
        return (
            jsonify({"error": "Se requiere un nombre en los parametros de la URL "}),
            400,
        )
    return jsonify({"mensaje": f"es palindromo?, {cadena == cadena[::-1]}"})

# agregamos cuenta una vocal en una cadena


if __name__ == '__main__':
    app.run()
    


