# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:13:01 2021

@author: Pipe
"""

diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

print (diccionario['nombre']) #Carlos
print (diccionario['edad'])#22
print (diccionario['cursos']) #['Python','Django','JavaScript']

print (diccionario['cursos'][0])#Python
print (diccionario['cursos'][1])#Django
print (diccionario['cursos'][2])#JavaScript

for key in diccionario:
  print (key, ":", diccionario[key])
  
#zip
dic = dict(zip('abcd',[1,2,3,4]))


# items()
# Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.
dic =   {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
items = dic.items()

# Crear una tabla con listas dentro del diccionario
Curso = {'Nombres' : ['Juan', 'Carlos', 'Pepe'], 'Apellidos' : ['Rodríguez', 'Martínez', 'Fernandez'], 'Notas' : [5, 4.5, 3]}

# keys()

# Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.

# dic =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# keys= dic.keys()

# keys→ [‘a’,’b’,’c’,’d’] 
# values()

# Retorna una lista de elementos, que serán los valores de nuestro diccionario.

# dic =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# values= dic.values()

# values→ [1,2,3,4] 
# clear()

# Elimina todos los ítems del diccionario dejándolo vacío.

# dic 1 =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# dic1.clean()

# dic1 → { }
# copy()

# Retorna una copia del diccionario original.

# dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# dic1 = dic.copy()

# dic1 → {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# fromkeys()

# Recibe como parámetros un iterable y un valor, devolviendo un diccionario que contiene como claves los elementos del iterable con el mismo valor ingresado. Si el valor no es ingresado, devolverá none para todas las claves.

# dic = dict.fromkeys(['a','b','c','d'],1)

# dic →  {‘a’ : 1, ’b’ : 1, ‘c’ : 1 , ‘d’ : 1}
# get()

# Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none.

# dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# valor = dic.get(‘b’) 

# valor → 2
# pop()

# Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.

# dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# valor = dic.pop(‘b’) 

# valor → 2
# dic → {‘a’ : 1, ‘c’ : 3 , ‘d’ : 4}
# setdefault()

# Funciona de dos formas. En la primera como get

# dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# valor = dic.setdefault(‘a’)

# valor → 1
# Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.

# dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# valor = dic.setdefault(‘e’,5)

# dic → {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4 , ‘e’ : 5}
# update()

# Recibe como parámetro otro diccionario. Si se tienen claves iguales, actualiza el valor de la clave repetida; si no hay claves iguales, este par clave-valor es agregado al diccionario.

# dic 1 = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# dic 2 = {‘c’ : 6, ’b’ : 5, ‘e’ : 9 , ‘f’ : 10}
# dic1.update(dic 2)

# dic 1 → {‘a’ : 1, ’b’ : 5, ‘c’ : 6 , ‘d’ : 4 , ‘e’ : 9 , ‘f’ : 10}

# entradas
salario_base, cantidad_horas_extra, hay_bonificacion = input().split()
sb, ch, hb = ListaEnt = ['500000', '8', '1']

