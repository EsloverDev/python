import sqlite3
from sqlite3 import Error
import datetime
conectar = sqlite3.connect('profesores.db') #recuerda usar un nombre distinto para la base de datos y otro para la tabla
curso = conectar.cursor()
#curso.execute('CREATE TABLE profesores(id integer PRIMARY KEY, nombre text, area text, salario real, edad integer)')
# curso.execute("INSERT INTO profesores VALUES(1, 'Mauricio', 'sociales', 800, 52)")
# curso.execute("INSERT INTO profesores VALUES(2, 'Esperanza', 'español', 600, 35)")
# curso.execute("INSERT INTO profesores VALUES(3, 'Lucas', 'fisica', 750, 47)")
# curso.execute("INSERT INTO profesores VALUES(4, 'Sandra', 'calculo', 900, 29)")
conectar.commit()
curso.execute('SELECT nombre FROM profesores where edad > 40')
rows = curso.fetchall()
for row in rows:
    print(row)
curso.execute('SELECT * FROM profesores')
rows = curso.fetchall()
print (len(rows))
curso.execute('create table if not exists proyectos(id integer, titulo text)')
conectar.commit()
#curso.execute('drop table if exists proyectos') # pilas, esto es para borrar la tabla
data = [(1, "Sistema Contable"), (2, "Agendamiento Citas"), (3, "Forensics"), (4, "Modulo nomina")]
curso.executemany("INSERT INTO proyectos VALUES(?, ?)", data) #Se ponen tantos ? como datos se vayan a insertar en la tabla
conectar.commit()
curso.execute('create table if not exists estudiante(id integer, nombre text, fecha_nacimiento date)')
data = [(1, "Juanito", datetime.date(2010, 1, 2)), (2, "Pedro", datetime.date(2012, 3, 4))]
curso.executemany("INSERT INTO estudiante VALUES(?, ?, ?)", data)
conectar.commit()
