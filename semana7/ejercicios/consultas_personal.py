# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

# insertamos nuevos departamento
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre, fecha_creacion)
    VALUES ('Ventas', '2020-04-11')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre, fecha_creacion)
    VALUES ('Marketing', '2020-04-11')
    """
)

# 3 nuevos cargos

conn.execute(
    """
    INSERT INTO CARGOS(nombre, nivel, fecha_creacion)
    VALUES('Gerente de Ventas', 'Senior', '2020-14-10')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS(nombre, nivel, fecha_creacion)
    VALUES('Analista de marketing', 'Junior', '2020-14-10')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS(nombre, nivel, fecha_creacion)
    VALUES('Representante de ventas', 'Junior', '2020-14-10')
    """
)
''''
# 2 nuevos empleados
conn.execute(
    """
    INSERT INTO EMPLEADOS(nombre, apellido_paterno, apellido_materno, fecha_contratacion)
    VALUES('Juan', 'Gonzales', 'Perez', '15-05-2023', '15-05-2023')
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS(nombre, apellido_paterno, apellido_materno, fecha_contratacion)
    VALUES('maria', 'Lopez', 'Martinez', '15-05-2023', '15-05-2023')
    """
)


'''
# 2 nuevos rempleados
conn.execute(
    """
    INSERT INTO EMPLEADOS(nombre, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
    VALUES('Juan', 'Gonzales', 'Perez', '15-05-2023','Ventas','Gerente de Ventas , '15-05-2023')
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS(nombre, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
    VALUES('maria', 'Lopez', 'Martinez', '15-05-2023','Marketing, 'Analista de Marketing, '15-05-2023')
    """
)


# nuevos registros salarios

conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion)
    VALUES(1, 3000, 2024-04-01, 2025-04-30, 2023-06-20 )
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion)
    VALUES(2, 3500, 2023-07-01, 2024-04-30, 2023-06-20 )
    """
)

# Lista los empleados y sus salarios


# Lista empleados el departamento en el que trabajan y el cargo que ocupan
print("\n EMPLEADOS")
cursor = conn.execute(
    """
    SELECT DEPARTAMENTOS.nombre, DEPARTAMENTOS.fecha_creacion, CARGOS.nombre, CARGOS.nivel, CARGOS.fecha_creacion
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = EMPLEADOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id =  EMPLEADOS.id
    """
)

# ACTUALIZAR
conn.execute(
    """
    UPDATE EMPLEADOS
    SET cargo_id = "Representante de ventas"
    WHERE id = 2
    """
)
# ACTUALIZAR
# ACTUALIZAR
conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE id = 2
    """
)
    
conn.commit()

conn.close()