import sqlite3
from sqlite3 import Error
conectadb =sqlite3.connect('mydatabase.db')
cursorObj = conectadb.cursor()
#cursorObj.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario real, area text, cargo text)")
# cursorObj.execute("INSERT INTO empleados VALUES(1, 'Jota', 700, 'RR.HH', 'Directos')")
# cursorObj.execute("INSERT INTO empleados VALUES(26, 'mario', 550, 'Programación', 'programador')")
cursorObj.execute('UPDATE empleados SET nombre= "Roberto" where id = 1')
conectadb.commit()
cursorObj.execute('SELECT * FROM empleados ')
rows = cursorObj.fetchall()
for row in rows:
    print(row)