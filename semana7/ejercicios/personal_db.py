# Importar módulo sqlite3
import sqlite3
# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

# tabla departamentos
try:
    conn.execute(
    """
    CREATE TABLE DEPARTAMENTOS(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
    );
    """
    )
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")

    
# tabla cargos
try:
    conn.execute(
    """
    CREATE TABLE CARGOS(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
    );
    """
    )
except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")
    
# tabla empleados
try:
    conn.execute(
    """
    CREATE TABLE EMPLEADOS(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        departamento_id INTEGER NOT NULL,
        codigo_id INTEGER NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREING (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREING (codigo_id) REFERENCES CARGOS(id) 
    );
    """
    )
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")
    
    # salarios


try:
    conn.execute(
    """
    CREATE TABLE SALARIOS(
        id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,

        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN (empleado_id) REFERENCES EMPLEADOS(id)
    );
    """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")


    
conn.commit()

conn.close()
