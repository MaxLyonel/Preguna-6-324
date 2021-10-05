# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:10:45 2021

@author: Usuario
"""

import psycopg2 as pc
conexion = pc.connect(
    user = "postgres",
    password = "admin",
    host = "127.0.0.1",
    port = "5432",
    database = "examen324"
    )

# =============================================================================
ci = 00000
cursor = conexion.cursor()
sql = "INSERT INTO docente(ci, nombre, paterno, materno) VALUES (%s, %s, %s, %s);"
datos = (100001, 'Otto', 'Simpson', 'Florida')
cursor.execute(sql, datos)
conexion.commit()
print("Insertado satisfactoriamente")
cursor.close()
conexion.close()
# =============================================================================


# =============================================================================
# # sql = "SELECT * FROM docente;"
# # cursor.execute(sql)
# # registros = cursor.fetchall()
# # for registro in registros:
# #     print('ci:', registro[0])
# #     print('nombre:', registro[0])
# #     print('paterno:', registro[1])
# #     print('materno:', registro[2])
# # =============================================================================