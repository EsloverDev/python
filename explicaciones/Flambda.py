"""
    Script3 para explicar funciones en Python.
    Funciones Anónimas

"""

# 1. Sitaxis -> lambda arguments: expression

triple = lambda x: x * 3

print((triple(3)))

##Notese que es el equivalente de 
#def triple(x):
#   return x * 3

# 2. Multiples parametros

suma = lambda num1, num2: num1 + num2

print(suma( 10, 20 ))

# 3. Usamos funciones lambda cuando requerimos una función sin nombre por un corto período de tiempo.
# Se usa en conjunto con funciones de orden superior como filter o map

# 3.1. Función filter: Se llama a la función con todos los elementos de la lista y se devuelve una nueva lista 
# que contiene elementos para los que la función se evalúa como Verdadero.

lista = [1, 5, 4, 6, 8, 11, 3, 12]

lista_filtrada = list(filter(lambda x: (x%3 == 0) , lista))

print(lista_filtrada)

# 3.2 Función map: Se llama a la función con todos los elementos de la lista y se devuelve una nueva lista 
# que contiene los elementos devueltos por esa función para cada elemento.

lista = [1, 2, 3, 4]

nueva_lista_map = list(map(lambda x: x ** 2 , lista))

print(nueva_lista_map)