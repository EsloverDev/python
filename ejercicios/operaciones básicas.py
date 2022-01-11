""" programa para hallar el cuadrado y cubo de un número
"""
# num = int(input("ingrese un número: "))

# cuadrado = num**2
# cubo = num**3

# print (f'el cuadrado del número {num} es {cuadrado}')
# print (f'el cubo del número {num} es {cubo}')

""" programa para hallar el perimetro y el area de un cuadrado
"""
# lado = int(input('ingrese la longitud de uno de los lados del cuadrado: '))

# area = lado ** 2
# perimetro = lado * 4

# print(f'el area del cuadrado es: {area}')
# print(f'el perimetro del cuadrado es: {perimetro}')

""" programa para encontrar el area de un triángulo
"""
# base = float(input('ingrese el tamaño de la base del triángulo: '))
# altura = float(input('ingrese el tamaño de la altura del triángulo: '))

# area = base * altura / 2

# print (f'el area del triángulo es: {area}')

""" programa para pasar de centímetros a metros y a milimetros
"""
# centimetro = int(input('ingrese la cantidad en cm: '))

# metro = centimetro / 100
# milimetro = centimetro * 10

# print(f'el valor en metros es de: {metro}m', f'y el valor en milimetros es de: {milimetro}mm')
# print('el valor en metros es de:', (metro),'m, y el valor en milimetros es de: '(milimetro),'mm')
""" programa para pasar de dias a siglos, años, meses y semanas
"""
# dias = int(input('ingrese la cantidad de dias: '))

# semanas = round((dias / 7),0)
# meses = round((dias / 30),0)
# años = round((dias / 365),0)
# siglos = round((dias / 36500),3)

# print(f'en total son: {semanas}, semanas')
# print(f'{meses} meses')
# print(f'{años} años')
# print(f'y {siglos} siglos')

"""programa para pasar de pesos colombianos a dólares americanos
"""
# cantidad =int(input('ingrese la cantidad en pesos: '))

# dolares = round((cantidad/3594),2)

# print(f'son : {dolares} dólares')

""" Solicitar 3 números (A,B,C) e imprimir
-	B*A-B*B/4*C
-	(A*B)/3*3
-	(((B+C)/2*A +10)*3*B)-6
"""
# A, B, C = float(input("ingrese primer numero: ")), float(input("ingrese segundo numero: ")), float(input("ingrese tercer numero: "))

# OP1=B*A-B*B/4*C
# OP2=(A*B)/3*3
# OP3=(((B+C)/2*A +10)*3*B)-6

# print(OP1)
# print(OP2)
# print(OP3)

""" formula de V en MRU es V=D/T
"""
# v = int(input("ingrese la velocidad dada en m/s: "))
# t = int(input("ingrese el tiempo dado en s: "))
# d = v*t
# print("La distancia es de: ", d, "m")

""" programa para determinar la media de tres numeros
"""
#num_1=float(input("ingrese primer numero: "))
#num_2=float(input("ingrese segundo numero: "))
#num_3=float(input("ingrese tercer numero: "))
#media=(num_1+num_2+num_3)/3

#print("la media es: ", media)
"""otra opción
"""
# num_1, num_2, num_3 = float(input("ingrese primer numero: ")), float(input("ingrese segundo numero: ")), float(input("ingrese tercer numero: "))

# media=(num_1+num_2+num_3)/3

# print("la media es: ", media)

""" programa que solicita el número de respuestas correctas = 3 puntos,
incorrectas = -1 punto y en blanco= 0 puntos de un examen de admisión
"""
# correcta = int(input("ingrese el número de respuestas correctas: "))
# incorrecta = int(input("ingrese el número de respuestas incorrectas: "))
# blanco = int(input("ingrese el número de respuestas en blanco: "))

# resultado = ((correcta*3) + (incorrecta*(-1)) + (blanco*0))

# print(f'el puntaje final es {resultado}')

"""micro discos 3.5 necesarios para hacer una copia de seguridad
"""
# pregunta = float(input('ingrese la capacidad expresada en Gb: '))

# gigas = pregunta *1024
# cantidad = round(gigas / 1.44),1

# print('En total se necesitan {} microdiscos.' .format(cantidad))

""" Dado el valor de un producto, hallar el ingreso general a las ventas
 y el precio de venta, teniendo en cuenta que Igv= PP*0.19 y PV=PP+Igv
"""
# pp = int(input('ingrese el precio del producto: '))

# igv = pp * 0.19
# pv = pp + igv

# print(f'el ingreso general a las ventas es de: {igv} y el precio de venta es de: {pv}.')

""" Dada una cantidad en pesos, imprimir su equivalente en dólares y euros,
teniendo en cuenta que un dólar =3.660 pesos y un euro= 4.481 pesos
"""
# pesos = int(input('ingrese una cantidad en pesos: '))

# dolar = round(pesos / 3660),3
# euro = round(pesos / 4481),3

# print(f'en total son {dolar} dolares, y {euro} euros')

"""a partir del tamaño de una tela cuadrada o rectangular, dividirla en tiras de 1mm de ancho
para formar una cuerda y al unir las tiras en una sola cuerda, formar un circulo y
determinar cuanto terreno podría abarcar
"""
# import math

# print('ingrese el largo y el ancho de la tela en metros respectivamente: ')
# largo, ancho = input().split()

# largo = float(largo)
# ancho = float(ancho)

# largo = 1000 * largo # pasando la medida a mm
# ancho = 1000 * ancho

# tiras = ancho #cantidad de tiras de 1mm de ancho
# cuerda = tiras * largo #longitud de la cuerda al unir todas las tiras

# pi = round(math.pi,4) #llamar la libreria math para seleccionar el valor de pi
# radio = cuerda / (2*pi)
# area = pi * (math.pow(radio,2)) #pow es para elevar un número x a la potencia y

# km = round((area * (1/100) * (1/10000) * (1/1000000)),2)

# print(f'El area de la circunferencia que podría redondear la cuerda en km^2 es de {km}')
