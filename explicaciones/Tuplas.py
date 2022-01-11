"""Script para explicar tuplas
    Netamente pedagogico"""

#TUPLA: COLECCION INMUTABLE (INMODIFICABLE) DE TAMAÑO FIJO CON DIFERENTES TIPOS DE DATOS

# TUPLA VACIA
t1 = ()
print(t1)
# LISTA VACIA
l1 = []
print(l1)
# TUPLA VACIA
t2 = tuple()
print(t2)

# saber el tamaño de una tupla
tamaño = len(t1)
print(tamaño)
print( len(l1))
print( len(t2))

#EJEMPLO

x = "ABC"
t1 = (1,2,3, x)
print(t1)
x = "XYZ"
print(t1)

tupla1 = (4, "Hola", 8.5, True, "L que quiero")
print(tupla1)

#  INFORMACION:       codigo,  nombre,       genero,    edad, altura, peso,  email,                   telefono
#  POSICION:            0,       1,              2,      3,    4,      5,     6,                       7
tupla_datos_persona = (95215,   "PEPITO PEREZ", "M",     43,   1.7,    81.4, "pepitoperez@gmail.com", "98097700")
print("CODIGO:", tupla_datos_persona[0])
print("NOMBRE:", tupla_datos_persona[1])
print("GENERO:", tupla_datos_persona[2])
print("EDAD:", tupla_datos_persona[3], " AÑOS")
print("ALTURA:", tupla_datos_persona[4], " Metros")
print("PESO:", tupla_datos_persona[5], "Kg")
print("EMAIL:", tupla_datos_persona[6])
print("TELEFONO:", tupla_datos_persona[7], "Telefono")

#Otra forma de crear una tupla
calificaciones = tuple(("logica y programacion","Pedro",2.5, 4.1, 5))
print("tupla_datos_persona es de tipo",type(tupla_datos_persona))
print("calificaciones es de tipo",type(calificaciones))
print(tupla_datos_persona)
print(calificaciones)

#RECORRER TUPLAS

print("MOSTRAR EL CONTENIDO DEL TUPLA")
print(tupla_datos_persona)

print("RECORRIDO DESDE 0 HASTA EL FIN DE 1 EN 1")
# recorrar desde el inicio hasta el final de uno en uno
for i in range(0, len(tupla_datos_persona ), 1):
  dato = tupla_datos_persona[i]
  print(i,".",dato)

print("RECORRIDO DESDE 0 HASTA EL FIN DE 1 EN 1")
# recorrar desde el inicio hasta el final de uno en uno pero abreviado
for i in range(len(tupla_datos_persona )):
  dato = tupla_datos_persona[i]
  print(i,".",dato)

print("RECORRIDO DESDE 0 HASTA EL FIN DE 2 EN 2")
# recorrar desde el inicio hasta el final de 2 en 2
for i in range(0, len(tupla_datos_persona ),2):
  dato = tupla_datos_persona[i]
  print(i,".",dato)

print("RECORRIDO INVERTIDO DESDE EL FIN HASTA EL INICIO")
# recorrar desde el inicio hasta el final de 2 en 2
for i in range(len(tupla_datos_persona )-1,-1,-1):
  dato = tupla_datos_persona[i]
  print(i,".",dato)

print("RECORRIDO DE EL INICIO HASTA EL FIN SIN INDICE")
# recorrar desde el inicio hasta el final de 2 en 2
cuenta = 0
for i in  tupla_datos_persona:
  print(cuenta,".",i)
  cuenta += 1

#UNPACKING O DESEMBALAJE
#Permite asignar cada elemento de la tupla a una variable individualmente
#las variables toman el mismo tipo de dato del elemento asignado en la tupla
#se deben usar el mismo numero de variables segun el numero de elementos de la tupla

codigo,  nombre, genero, edad, altura, peso,  email, telefono = tupla_datos_persona
print("CODIGO:", codigo)
print("CODIGO:", tupla_datos_persona[0])
print("NOMBRE:", nombre)
print("GENERO:", genero)
print("EDAD:", edad, " AÑOS")
print("ALTURA:", altura, " Metros")
print("PESO:", peso, "Kg")
print("EMAIL:", email)
print("TELEFONO:", telefono)

#UNPACKING

edad1 = 43
esatatura1 = 1.72
print("EDAD:",edad1, "-TIPO: ",type(edad1))
print("ESTATURA:",esatatura1, "-TIPO: ",type(esatatura1))
datos = (edad1, esatatura1)
print("DATOS:",datos, "- TIPO: ",type(datos))
edad2, estatura2 = datos
print("EDAD:",edad2, "-TIPO: ",type(edad2))
print("ESTATURA:",estatura2, "-TIPO: ",type(estatura2))

#EJEMPLO

x = (10,"A", True)
print("X es de tipo:", type(x))
print("La tupla X tiene:", len(x), "elemento")

#UNIENDO DOS TUPLAS
datos2 = datos + x 
print("Los datos de la nueva tupla son: ",datos2)

#QUE ESTAMOS HACIENDO AQUI?
datos3 = datos * 5
print(datos3)

#Y AQUI?
t1 = ("a", 10, True, 10)
t2 = ("a", 10, False, 10)
print(t1.index(10))

#El método count() cuenta el número de veces que el objeto pasado como parámetro se ha encontrado en la lista.
#El método index() busca el objeto que se le pasa como parámetro y devuelve el índice en el que se ha encontrado.
#El método index() también acepta un segundo parámetro opcional, que indica a partir de que índice empezar a buscar el objeto.
print(t1.count(10))
if t1 == t2:
  print(t1,"y",t2,"SI son igules")
else:
    print(t1,"y",t2,"NO son igules")

#Tuplas anidadas
tupla = 1, 2, ('a', 'b'), 3
print(tupla)            #(1, 2, ('a', 'b'), 3)
print(tupla[2][0])      #a

#Convirtiendo a tuplas
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla))      #<class 'tuple'>
print(tupla)            #(1, 2, 3)

#Y se puede también asignar el valor de una tupla con n elementos a n variables.
l = (1, 2, 3)
x, y, z = l
print(x, y, z)          #1 2 3

