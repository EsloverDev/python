""" Sean A, B, C, las ventas de 3 productos imprimir: -la venta más alta, -la venta más baja,
la media de los productos
"""
# A, B, C =input('ingrese los valores de las ventas de los tres productos separados por un espacio: ').split()

# A = int(A)
# B = int (B)
# C = int (C)

# if A > B and A > C and B > C:
#     print(f'la venta más alta es {A}, y la más baja es {C}')
# elif A > B and A > C and C > B:
#     print(f'la venta más alta es {A}, y la más baja es {B}')
# elif B > C and B > A and A > C:
#     print(f'la venta más alta es {B}, y la más baja es {C}')
# elif B > C and B > A and C > A:
#     print(f'la venta más alta es {B}, y la más baja es {A}')
# elif C > A and C > B and A > B:
#     print(f'la venta más alta es {C}, y la más baja es {B}')
# elif C > A and C > B and B > C:
#     print(f'la venta más alta es {C} y la más baja es {A}')
    
# media = (A + B + C) / 3

# print(f'la media de las ventas es {media}')

""" Programa que pide la longitud de los 3 lados de un triángulo e imprime si es
equilátero(3 lados iguales) isósceles(Dos lados iguales) o escaleno(3 lados diferentes)
"""
# lado_a, lado_b, lado_c = input('ingrese la longitud de los lados del triángulo separadas por un espacio: ').split()

# lado_a = float(lado_a)
# lado_b = float(lado_b)
# lado_c = float(lado_c)

# if lado_a == lado_b == lado_c:
#     print('es un triángulo equilátero.')
# elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
#     print('es un triángulo isósceles.')
# else:
#     print('es un triángulo escaleno')

""" Programa que pide el tamaño de un tornillo y lo imprime teniendo en cuenta las siguientes
condiciones: entre [1cm, 3cm) = pequeño [incluido], (no incluido), [3cm, 5cm) = mediano, 
[5cm, 6.5cm) = grande, [6.5cm, 8.5cm) = muy grande, [8.5cm, en adelante) = gigante.
"""
# tamaño = float(input('ingrese el tamaño del tornillo dado en cm: '))

# if tamaño < 1:
#     print ('no existe')
# elif tamaño >= 1 and tamaño < 3:
#     print('pequeño')
# elif tamaño >= 3 and tamaño < 5:
#     print('mediano')
# elif tamaño >= 5 and tamaño < 6.5:
#     print('grande')
# elif tamaño >= 6.5 and tamaño < 8.5:
#     print('muy grande')
# else:
#     print('gigante')

"""Programa que pide tres numeros y determina si dos son iguales, tres son iguales,
o todos son diferentes
"""
# n = float(input("ingrese el primer número "))
# m = float(input("ingrese el segundo número "))
# k = float(input("ingrese el tercer número "))
# if n==m==k:
#     print("los tres son iguales")
# elif n==m!=k or n==k!=m or m==k!=n:
#     print("hay dos iguales")
# else:
#     print("todos los números son diferentes")

"""programa para determinar cual es el mayor de dos números y saber si el número mayor es 
múltiplo del menor.
"""
# n = int(input("ingrese el primer número "))
# m = int(input("ingrese el segundo número "))

# if n<m and m%n == 0:
#     print(m,"es el mayor y es múltiplo de ", n)
# elif n>m and n%m == 0:
#     print(n, "es el mayor y es múltiplo de ", m)
# elif n<m and m%n != 0:
#     print(m,"es el mayor y no es múltiplo de ", n)
# elif n>m and n%m != 0:
#     print(n,"es el mayor y no es múltiplo de ", m)
# else:
#     print("los números son iguales")
# print('¿quiere intentarlo otra vez?')

""" Programa que pregunta si quiere calcular el área de un triángulo o la de un circulo.
"""
# import math
# print('Escriba "T" o "t" para triángulo, o "C" o "c" para circulo y calcularé el área: ')

# respuesta = input()

# if respuesta == "T" or respuesta == "t":
#     #b, a = float(input('ingrese la base y la altura correspondientemente separados por un espacio: ')).split()
#     b = float(input('ingrese la base: '))
#     a = float(input('ingrese la altura: '))
#     triangulo = b*a/2
#     print(f'El área del triángulo es: {triangulo}')
# elif respuesta == "C" or respuesta == "c":
#     r = float(input('ingrese el radio: '))
#     circulo = round((math.pi)*(math.pow(r,2)),2)
#     print(f'El área del circulo es: {circulo}')
# else:
#     print('datos incorrectos, digite "T", "t", "C", o "c".')

""" Programa que pide un número y si es múltiplo de 1000 imprime
'Felicidades ganaste un premio'.
"""
# num = int(input('Digite un número: ' ))

# if num%1000 == 0:
#     print('Felicidades ganaste un premio')
# else:
#     print('sigue intentando')

""" Programa que pide un día de la semana e imprime: si es lunes, sábado o domingo = 'hoy es un gran día', 
si es viernes = 'ya vemos cerca el fin de semana', de lo contrario = 'avancemos que ya es: '
"""
# dia = input('Digite un día de la semana en letra minúscula: ')

# if dia == 'lunes' or dia == 'sabado' or dia == 'domingo':
#     print(f'{dia}: hoy es un gran día')
# elif dia == 'viernes':
#     print(f'{dia}: ya vemos cerca el fin de semana')
# elif dia == 'martes' or dia == 'miercoles' or dia == 'jueves':
#     print(f'avancemos que ya es: {dia}')
# else:
#     print(f'"{dia}": no es un día de la semana.')
