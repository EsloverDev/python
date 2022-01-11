"""Script para explicar la forma de conectar python con SQLite3
    Intenciones netamente educativas"""
# Visualizador de SQLite: https://github.com/sqlitebrowser/sqlitebrowser/releases/tag/v3.11.0-beta3
#Para poder empezar a usar debemos importar SQLite
import sqlite3
from sqlite3 import Error
conectadb = sqlite3.connect('mydatabase.db')

#Para realizar y ejecutar sentencias de SQLite en Python, se necesita un objeto cursor. Se puede crear utilizando el método cursor().
#El SQLite3 cursor es un método del objeto de conexión. Para ejecutar sentencias de SQLite3, primero se establece una conexión y luego 
# se crea un objeto cursor utilizando el objeto de conexión de la siguiente manera:
cursorObj = conectadb.cursor()

#Cuando creamos una conexión con SQLite(linea 6), un archivo de base de datos se crea automáticamente si no existe ya. 
# Este archivo de base de datos se crea en el disco, pero también podemos crear una base de datos en la RAM usando :memory:
#por ejemplo

# def sql_connection():
#     try:
#         conectadb = sqlite3.connect(':memory:')
#         print("Conexion establecida, la base de datos ha sido creada en memoria")
#         return conectadb
#     except Error:
#         print(Error)
    # finally: #Cerrar una conexión es opcional, pero es una buena práctica de programación, de esta forma liberas la memoria de los recursos no utilizados.
    #     conectadb.close()
# sql_connection()

#Crear una tabla(Ver archivo de la clase)
#Crearemos una tabla empleados
#Este método crea un objeto cursor para ejecutar la sentencia de create table.
# def sql_connection():

#     try:
#         conectadb = sqlite3.connect('mydatabase.db')
#         return conectadb
#     except Error:
#         print(Error)

#Podemos crear una funcion para las ejecutar las sentencias de sql 
#def sql_table(conectadb):

cursorObj = conectadb.cursor()
#cursorObj.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario real, area text, cargo text)")
# conectadb.commit()
#El método commit () guarda todos los cambios que hacemos. Al final, se llaman ambos métodos.

#conectadb = sql_connection()
# sql_table(conectadb)
#Para insertar en una tabla usamos INSERT INTO
# o simcplemente las ejecutamos asi 
cursorObj = conectadb.cursor()
cursorObj.execute("INSERT INTO empleados VALUES(1, 'Jota', 700, 'RR.HH', 'Director')")
#conectadb.commit()

#Actualiza tabla(Ver documento clase)
cursorObj = conectadb.cursor()
cursorObj.execute('UPDATE empleados SET nombre = "Roberto" where id = 1')
conectadb.commit()

#Seleccionar datos(Ver docuemtno clase)
cursorObj.execute('SELECT * FROM empleados ') # Toda la tabla
cursorObj.execute('SELECT name, salario FROM empleados ') # columnas especificas
cursorObj.execute('SELECT name, salario FROM empleados where salario >100 ') # columnas especificas con el filtro aplicado
#Si deseamos que nos muestre la consulta seria :
rows = cursorObj.fetchall()
#y para imprimirlo
for row in rows:
    print(row)
#También podemos usar el fetchall () en una línea de la siguiente manera:
#[print(row) for row in cursorObj.fetchall()]

#Ahora vamos a insertar varios empleados en la tabla empleados e imprimiremos aquellos en los que el salario es menor a 700
