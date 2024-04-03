#importamos mudulo de aqlite 3
import sqlite3
# Crear conexion a la base de datos
conn = sqlite3.connect("restaurante.db")

'''
● Con DB de RESTAURANTE
● Encuentra todos los pedidos realizados junto con los nombres de los
platos y los números de mesa (JOIN)
● Encuentra todos los platos que han sido pedidos, incluso aquellos
que no se han pedido aún (LEFT JOIN)
'''


# Consultar datos de matriculación INNER JOIN
print("\nPEDIDOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PLATOS.precio, PLATOS.categoria, MESAS.numero, PEDIDOS.fecha
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)
    
# Consultar datos de matriculación LEFT JOIN
print("\nPEDIDOS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre
    FROM PLATOS
    LEFT JOIN PEDIDOS ON PLATOS.id = PEDIDOS.plato_id
    """
)
for row in cursor:
    print(row)
