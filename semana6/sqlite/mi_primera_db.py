# Importar modulo sqlite3
import sqlite3
# Crear conexion a la base de datos
conn = sqlite3.connect("instituto.db")
# Crear tabla de carreras 
conn.execute(
    """
    CREATE TABLE CARRERAS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL);
    """
)

#insertar datos de carreras
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion)
    VALUES ('Ingenieria en Informatica', 5)
    """
)
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion)
    VALUES ('Licenciatura en Administracion', 4)
    """
)

# Consultar datos
print("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)
    
# Crear tabla de estudiantes
conn.execute(
    """
    CREATE TABLE ESTUDIANTES
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL);
    """
)

# insertamos datos de estudiantes
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento)
    VALUES ('Juan', 'Perez', '2000-05-15')
    """
)

conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento)
    VALUES ('Maria', 'Lopez', '1999-08-20')
    """
)

# Consultar datos
print("\nESTUDIANTES:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)
    
    
# Crear tabla de matriculas
conn.execute(
    """
    CREATE TABLE MATRICULAS
    (id INTEGER PRIMARY KEY,
    estudiante_id INTEGER NOT NULL,
    carrera_id INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
    FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
    """
)

# insertamos datos de matriculas
conn.execute(
    """
    INSERT INTO MATRICULAS (estudiante_id, carrera_id, fecha)
    VALUES (1, 1, '2024-01-15')
    """
)

conn.execute(
    """
    INSERT INTO MATRICULAS (estudiante_id, carrera_id, fecha)
    VALUES (2, 2, '2024-01-20')
    """
)

conn.execute(
    """
    INSERT INTO MATRICULAS (estudiante_id, carrera_id, fecha)
    VALUES (1, 2, '2024-01-25')
    """
)

# Consultar datos
print("\nMATRICULAS:")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULAS.fecha
    FROM MATRICULAS
    JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id
    JOIN CARRERAS ON MATRICULAS.carreera_id = CARRERAS.id
    """)
for row in cursor:
    print(row)
    
    
# Listar datos de matriculacion
print("\nMATRICULAS:")
cursor = conn.execute(
    """
    SELECT * FROM MATRICULAS
    """)
for row in cursor:
    print(row)
    
#actualizar una fila de la tabla de matriculacion
conn.execute(
    """
    UPDATE MATRICULAS
    SET fecha = '2024-01-30'
    WHERE id = 2
    """
)
for row in cursor:
    print(row)
    
  
# Eliminar
conn.execute(
    """
    DELETE FROM MATRICULAS
    WHERE id = 1
    """
)  
for row in cursor:
    print(row)
    
# Cerrar conexion
conn.close()

