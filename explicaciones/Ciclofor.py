"""
    Script que explica los ciclos for.
    Estructura:

    for variable in iterable:
        cuerpo del bucle
"""


""" 1. Definición básica """

# print("Empieza el Ciclo")
# for i in [0, 1, 2]:
#     print("Ciclo num {}".format(i))
# print("Finaliza el ciclo")

""" i se conoce como variable de control """

"Que sucede en el siguiente ejemplo:"
# print("Empieza el Ciclo")
# for i in []:
#     print("Ciclo num {}".format(i))
# print("Finaliza el ciclo")

"i se conoce como variable de control"
# print("Empieza el Ciclo")
# for _ in [0, 1, 2]:
#     print("Hola Mundo!", end=" ")
# print("Finaliza el ciclo")

""" 2. Función range
Para generar secuencias de números.
range(start,stop,step size) """
# for i in range(10):
#     print("Imprimir var {}".format(i)) # 10 veces se ejecuta


# for i in range(2,10):
#     print("Imprimir var {}".format(i)) # 8 veces se ejecuta


# for i in range(2,10,3):
#     print("Imprimir var {}".format(i)) # 3 veces se ejecuta


# for j in range(10,100,10):
#     print("Imprimir var {}".format(j)) # 9 veces se ejecuta

"""4. Función len()"""

#nombre = ["Jairo","Natalia","Nicolas","Sofia","Marcel","Juan", "Ruben", "Pacho","Maria","Judit","David", "Leonardo", "Leonora","Martín"]

"""Opción 1 para recorrer la lista nombre"""

# for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13]:
#     print("Mi nombre es {}".format(nombre[i]))

"""Opción 2 usar la funcion len y combinarla con range"""

#print(len(nombre)) # 14

#for i in range(len(nombre)):
    #print("Mi nombre es {}".format(nombre[i]))


"""5. Contador con ciclo for """

# cuenta = 0
# for i in range(1, 101):
#     if i % 6 == 0:
#         cuenta = cuenta + 1
# print("Desde 1 hasta 100 hay {} múltiplos de 6".format(cuenta))


"""6. Acumulador con ciclo for"""

suma = 0
for i in range(1, 101):
    suma += i
print("La suma de los 100 primero números naturales es {}".format(suma))

suma = 0
for n in range(50):
    suma = suma + n
print("TOTAL:",suma)
print("Bye Bye")