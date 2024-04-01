import sqlite3
conn = sqlite3.connect("restaurante.db")
# Creamos la tabla de platos
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL,
    categoria TEXT NOT NULL);
    """
)

# insertamos datos de platos
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('Sajta', 20, 'Principal')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('Sopa de mani', 10, 'entrada')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('Ensalada Rusa', 25, 'entrada')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('Ensalada de verduras', 20, 'Saludable')
    """
)
#consultar datos de platos
print("Platos: ")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    

conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)
# insertamos datos para las mesas
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (12)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (6)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (10)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (24)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (48)
    """
)
# Consulamos datos de las mesas
print("\nMesas: ")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

# Creamos la tabla de pedidos
conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato_id INTEGER NOT NULLL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
    FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
    """
)
# insertamos datos de los pedidos
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (1, 4, 3, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (2, 3, 2, '2024-04-01')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (3, 2, 4, '2024-04-01')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (4, 1, 1, '2024-04-01')
    """
)

# consultados datos de los pedidos
print("\nPEDIDOS:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PLATOS.precio, PLATOS.categoria, MESAS.numero
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
    )
for row in cursor:
    print(row)
