""" Programa que almacena las asignaturas de un curso en una lista y la
muestra por pantalla con la frase “yo estudio”.
"""
# cuantas = int(input('¿cúantas materias quiere ingresar?: '))
# asignaturas = []

# for i in range(cuantas):
#     a = input('ingrese la asignatura: ')
#     asignaturas.append(a)
# for a in range(len(asignaturas)):
#     print(f'yo estudio: {asignaturas[a]}')

""" Programa que almacena las asignaturas de un curso en una lista, pregunta
al usuario la nota que ha sacado en cada asignatura, y después las muestra por
pantalla con el mensaje "En <asignatura> has sacado <nota>".
"""
# cuantas = int(input('¿cúantas materias quiere ingresar?: '))
# materias = []
# for i in range(cuantas):
#     asignatura = input('Digite el nombre de la asignatura: ')
#     materias.append(asignatura)

# notas = []

# for i in materias:
#     calificacion = float(input(f'¿cuál fue su calificación en {i}?: '))
#     notas.append(calificacion)

# posicion = 0
# # for i in range(len(notas)): no funciona porque la posicion i siempre va a avanzar a medida que los valores de la lista disminuyen
# while posicion < len(notas):
#     if notas[posicion] >= 3.0:
#         notas.pop(posicion)
#         materias.pop(posicion)
#     else:
#         posicion+=1
# for i in range(len(materias)):
#     print(f'la materia que debe habilitar es {materias[i]}')
#     print(f'En asignatura {materias[i]} ha sacado {notas[i]}.')

""" Programa que pregunta al usuario los números ganadores de la lotería
primitiva, los almacena en una lista y los muestra por pantalla ordenados
de menor a mayor.
"""
# n1, n2, n3, n4, n5, n6 = input('ingrese los números ganadores de la loteria: ').split()[:6]
# n1 = int(n1)
# n2 = int(n2)
# n3 = int(n3)
# n4 = int(n4)
# n5 = int(n5)
# n6 = int(n6)

# ganadores = []
# ganadores.append(n1)
# ganadores.append(n2)
# ganadores.append(n3)
# ganadores.append(n4)
# ganadores.append(n5)
# ganadores.append(n6)

# ganadores.sort() #ordena los elementos de una lista
# print(ganadores)

""" Programa para rellenar una lista de 15 número enteros con valores aleatorios
entre 1 y 10, y dice cuantos pares e impares hay, cuanto suman los múltiplos de 3 ingresados.
"""
# import random
# numeros = []
# for i in range(0, 15):
#     aleatorio = random.randint(1,10)
#     numeros.append(aleatorio)
# print(numeros)

# m_3 = 0
# par = 0
# impar = 0
# for i in range(len(numeros)):
#     if i%3 == 0:
#         modulo3 = i%3
#         m_3 = m_3 + numeros[i]
# print(f'la suma de los números que están en una posición múltiplo de 3 es: {m_3}')
# for i in numeros:
#     if i%2 == 0:
#         par += 1
#     else:
#         impar += 1
# print(f'en total son {par} pares y {impar} impares.') # dice cuantos pares e impares hay

""" Los primeros 15 valores de la serie de fibonacci.
"""
# fibo = [1, 1]
# for i in range(13):
#     fibo.append(fibo[i]+fibo[i+1])
# print(f'los primeros 15 valores de la serie de Fibonacci son: {fibo}')
""" Programa que pide 15 números y los imprime desde el último hasta el primero
y también los imprime en orden creciente.
"""
# lista = input('digite 15 números separados cada uno por un espacio: ').split()[ :15]
# numeros = list(lista)
# print(numeros)
# inv = numeros[-1: :-1]
# for i in inv:
#     print(i, end=" ")
# numeros.sort() # sirve para ordenar los números en orden creciente
# print(numeros)

""" Programa que pide 15 números, que no deben estar repetidos, los introduce
en una lista y los imprime.
"""
# lista = []
# numeros = int(input('ingrese un número: '))
# lista.append(numeros)
# i = 1

# while i < 15:
#     bandera = 0
#     numeros = int(input('ingrese un número: '))
#     for j in lista:
#         if j == numeros:
#             bandera = 1

#     if bandera != 1:
#         lista.append(numeros)
#     else:
#         print('número repetido, por favor ingrese otro número.')
#         i -= 1
#     i += 1
# print(lista)

""" Programa que pide un número e imprime el nombre de cada uno de los dígitos
"""
# numero = input('ingrese un número: ')
# lista = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
# agrega = []

# for i in numero:
#     agrega.append(i)
    
# for j in agrega:
#     if j != "0" and j != "1" and j != "2" and j != "3" and j != "4" and j != "5" and j != "6" and j != "7" and j != "8" and j != "9":
#         print('Éste no es un número.')
#     else:
#         j = int(j)
#         print(lista[j], end=" ")

""" Programa que almacena en una lista las notas ingresadas por los estudiantes de un
grupo de 10 personas e imprime los siguientes intervalos [0, 5) = insuficiente,
[5, 7) = Aprobado, [7, 9) = Notable, [9, 10] = excelente.
"""
# notas = input('ingrese máximo 10 notas separadas por un espacio: ').split()[ :10]
# insuficiente = []
# aprobado = []
# notable = []
# excelente = []
# ins = 0
# ap = 0
# no = 0
# exc = 0

# for i in notas:
#     i = float(i)
#     if i >= 0 and i < 5:
#         insuficiente.append(i)
#         ins += 1
#     elif i >= 5 and i < 7:
#         aprobado.append(i)
#         ap += 1
#     elif i >= 7 and i < 9:
#         notable.append(i)
#         no += 1
#     else:
#         excelente.append(i)
#         exc += 1
# print(f'la cantidad de notas son: excelente = {exc}, {excelente}, \nnotable = {no}, {notable}, \naprobado = {ap}, {aprobado}, \ninsuficiente = {ins}, {insuficiente}.')
