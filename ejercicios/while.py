""" Programa para pedir la contraseña correcta
"""
# contraseña = input("ingrese la contraseña: ")

# while contraseña != "lovepython123":
#     print("contraseña incorrecta")
#     contraseña = input("ingrese la contraseña nuevamente: ")

# if contraseña == "lovepython123":
#     print('continue')

""" Programa que solicita números enteros siempre y cuando sean
menores de 10 e imprime la multiplicación de cada uno de los números
digitados(3*5*6*3..). Cuando se digite un numero mayor de 10 imprime la
multiplicación que lleva hasta el momento
"""
# num = int(input('digite un número < 10: '))
# mult = 1

# while num < 10:
#     mult *= num
#     num = int(input('digite otro número <= 10 para multiplicarlo o > 10 para ver el resultado: '))
# print(mult)

""" Programa que lee los números que se le ingresan y termina cuando el numero
sea cero, al final imprime la suma de los números ingresados
"""
# num = float(input('digite un número: '))
# sum = 0

# while num != 0:
#     sum += num
#     num = float(input('digite otro número para sumarlo o digite 0 para ver el resultado: '))
# print(sum)

""" Programa que pide las notas referentes a un curso (no sabemos cuantas son),
termina cuando ingresa -1 y al final imprime el promedio de las notas ingresadas
"""
# nota = float(input('ingrese la calificación: '))
# suma = 0
# i = 0
# while nota != -1:
#     suma += nota
#     i += 1
#     nota = float(input('ingrese otra calificación o digite -1 para ver el promedio: '))
# print(f'el promedio es: {suma/i}')

""" Programa que simula una alcancía o hucha, solicita el objetivo y va solicitando
una y otra vez el dinero, acumulando el valor que se ingresa hasta completar el objetivo.
"""
# objetivo = float(input('¿cuánto quieres ahorrar?: '))
# acum = 0

# while acum < objetivo:
#     ingreso = float(input('¿cuánto vas a ahorrar hoy?: '))
#     acum += ingreso
# print(f'alcanzaste tu objetivo: {acum} felicitaciones.')

""" Programa que solicita al usuario el valor de cada una de sus compras (No sabemos
cuántas compras hizo), si ingresa valores negativos no los toma en cuenta y vuelve a
pedirlo y termina cuando se digita el monto=0 e imprime el total de las compras realizadas
"""
# compras = int(input('ingrese el valor de su compra: '))
# total = 0

# while compras != 0:
#     if compras < 0:
#         print('valor errado')
#     else:
#         total += compras
#     compras = int(input('ingrese el valor de otra compra o digite 0 para ver el total: '))
# print(total)

""" Programa que calcula el factorial de un numero > 0 y < 20.
"""
# import math
# n = int(0) # aquí se inicializan las variables, se pueden inicializar con cualquier
# bandera = 1 # número ya que en el ciclo while se van a renombrar, esto solo se usa para que la variable entre en el ciclo.

# while bandera == 1:
#     n = int(input('ingrese un número entero > 0 y < 20 para calcular su factorial: '))
#     if n > 0 or n < 20:
#         factorial = math.factorial(n)
#         bandera = 0
# print(f'el factorial del número {n} es: {factorial}')

""" Programa que genera números aleatorios entre 1 y 100, y sale cuando el número es = 25
"""
# import random

# while True:
#     aleatorio = random.randrange(1, 101)
#     print (aleatorio)
#     if aleatorio == 25:
#         print ("FIN DEL CICLO")
#         break

""" Programa que pide la cantidad de perfiles de hierro a procesar e ingrese la longitud
de cada perfil sabiendo que las que miden entre 1.20 y 1.30 son aptas, e imprime la cantidad
de piezas que son aptas.
"""
# cantidad = int(input('¿cuántos perfiles de hierro quiere analizar?: '))
# total = 0

# while cantidad > 0:
#     perfiles = float(input('ingrese la medida del perfil de hierro que quiere analizar: '))
#     if perfiles < 1.20 or perfiles > 1.30:
#         print('Ésta medida no es apta.')
#     elif perfiles >= 1.20 or perfiles <= 1.30:
#         total += 1
#     cantidad -=1
# print(f'la cantidad de piezas aptas son : {total}')

""" Programa que lee los sueldos de cada empleado que oscilan entre $100 y $500 e informa
cuantos cobran entre $100 y $300 y cuantos cobran más de $300. Además informa cuánto es el
total de la nómina.
"""
# empleados = int(input('¿cuántos empleados quiere analizar?: '))
# rango_1 = 0
# rango_2 = 0
# nomina = 0

# while empleados > 0:
#     sueldo = float(input('ingrese el sueldo: '))
#     if sueldo >= 100 and sueldo <= 300:
#         rango_1 += 1
#         nomina += sueldo
#         empleados -= 1    
#     elif sueldo > 300 and sueldo <= 500:
#         rango_2 += 1
#         nomina  += sueldo
#         empleados -= 1
#     else:
#         print('está por fuera del rango de sueldos.')        
# print(f'hay {rango_1} empleados que cobran entre $100 y $300,\ny {rango_2} empleados que cobran más de $300,\nademás el total de la nómina es de {nomina}')
