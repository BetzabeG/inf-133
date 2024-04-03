#importamos mudulo de aqlite 3
import sqlite3
# Crear conexion a la base de datos
conn = sqlite3.connect("restaurante.db")
# Consultar datos de matriculación INNER JOIN
print("\nPEDIDOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT * 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)
    
# Consultar datos de matriculación LEFT JOIN
print("\nPEDIDOSLEFT JOIN:")
cursor = conn.execute(
    """
    SELECT *
    FROM PLATOS
    LEFT JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id;
    """
)
for row in cursor:
    print(row)
