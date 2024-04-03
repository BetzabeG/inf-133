import sqlite3
conn = sqlite3.connect("restaurante.db")
# Creamos la tabla de platos
try :
    conn.execute(
    """
    CREATE TABLE PLATOS(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT NOT NULL);
    """
)
except sqlite3.OperationalError:
    print("La tabla PLATOS ya existe")    


# insertamos datos de platos
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('Pizza', 10.99, 'Italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('Hamburguesa', 8.99, 'Americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('Sushi', 12.99, 'Japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('Ensalada', 6.99, 'Vegetariana')
    """
)
#consultar datos de platos
print("Platos: ")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    
# crear tabla para mesas
try:
    conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)
except sqlite3.OperationalError:
    print("La tabla MESAS ya existe")
    

# insertamos datos para las mesas
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (4)
    """
)

# Consulamos datos de las mesas
print("\nMesas: ")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

# Creamos la tabla de pedidos
try:
    conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
    FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
    """
)
except sqlite3.OperationalError:
    print("La tabla CARRERAS ya existe")
    

# insertamos datos de los pedidos
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (1, 2, 2, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (2, 3, 1, '2024-04-01')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (3, 1, 3, '2024-04-01')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (4, 4, 1, '2024-04-01')
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
    
# Actualiza el precio del plato con id 2 (Hamburguesa) a 9.99
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)
for row in cursor:
    print(row)

# Cambia la categoria del plato con id 3 (Sushi) a "Fusion"
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusion'
    WHERE id = 3
    """
)
for row in cursor:
    print(row)
    
    
# Elimina el pedido con id 3
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)
for row in cursor:
    print(row)
    
    
#Confirmar cambios
conn.commit()
    
# Cerrar conexion
conn.close()

