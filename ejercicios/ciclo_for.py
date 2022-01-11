""" Programa que realiza iteraciones en un rango de 1 a 10 e imprime en cada
iteración un mensaje y el numero en el que va, realizar también la variación de ciclo para
que en vez de avanzar, retroceda; es decir empiece en 10 y llegue a 1.
"""
# for i in range (1,11):
#     print(f'ya vamos en el {i}')
# for i in range (10,0,-1):
#     print(f'ya vamos en el {i}')

""" la tabla del 7 hasta el 15
"""
# for i in range(0,16):
#     print (f'7 x {i} = {i*7}')

""" Programa en el que dado un número natural de latas introducido por el usuario,
se comprueba si es adecuado o no para apilarlas de forma triangular.
"""
# cantidad = int(input('¿cuantas latas tiene para apilarlas en forma triangular?: '))
# num_ant = 0
# num_sig = 1

# for i in range(2,cantidad):
#     num_sig = num_sig + num_ant
#     num_ant = i
#     if num_sig == cantidad:
#         print('si es adecuado para apilar')
#         break
#     elif num_sig > cantidad:
#         print('no adecuado')
#         break    

""" Programa que imprime la tabla de multiplicar que ud quiera máximo hasta el 10,
y hasta el número que ud quiera.
"""
# tabla = int(input('¿cuál tabla de multiplicar quiere que imprima? máximo hasta el 10: '))

# while tabla < 1 or tabla > 10:
#     print('sólo imprimo las tablas del 1 al 10.')
#     tabla = int(input('digite una tabla de multiplicar máximo hasta el 10: '))

# limitei = int(input('¿desde cuál número quiere empezar a multiplicar?: '))
# limitef = int(input('¿hasta qué número quiere que la imprima?: '))

# while limitef < limitei:
#     print(f'debe digitar un número mayor que {limitei} porque solo las imprimo en orden ascendente.')
#     limitef = int(input('¿hasta qué número quiere que la imprima?: '))

# for i in range(limitei,limitef+1):
#     print(f'{tabla} x {i} = {tabla*i}')

""" Programa que pregunta cuántos números va a ingresar, pida esos
números, y muestra un mensaje cada vez que un número no sea mayor que el
primero.
"""
# num = int(input('¿cuántos números va a ingresar?: '))
# primero = int(input('ingrese el primer número: '))
# for i in range(1,num):
#     siguiente = int(input(f'ingrese un número más grande que {primero}: '))
#     if siguiente < primero:
#         print(f'este número no es mayor que {primero}')

""" Programa que pide dos números enteros y escribe la suma de todos los enteros que hay
desde el primer número hasta el segundo.
"""
# inicio = int(input('ingrese el primer número: '))
# fin = int(input('ingrese el segundo número: '))
# suma = 0

# if inicio < fin:
#     for i in range(inicio,fin+1):
#         suma = suma + i #acumulador
# else:
#     for i in range(fin,inicio+1):
#         suma = suma + i #acumulador
# print(suma)

""" Programa que pregunta al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión cada año que dura la inversión.
"""
# cantidad = int(input('¿cuánto quiere invertir?: '))
# interes = int(input('¿cuál es el interes anual?: '))
# tiempo = int(input('¿cuántos años?: '))

# for i in range(tiempo):
#     cantidad *= 1 +interes/100 #buscar la fórmula del interés compuesto
#     print(f'el capital obtenido en el año {i+1} es de {cantidad}.')

""" Programa que pide un número entero y muestra por pantalla un triángulo rectángulo
de altura el número introducido.
"""
# altura = int(input('ingrese la altura del triángulo: '))

# for i in range(1,altura+1):
#     print('*'*i)

""" Programa que pide al usuario un número entero y muestra por pantalla
un triángulo rectángulo de altura la mitad del número introducido.
"""
# altura = int(input('digite la altura del triángulo: '))

# for i in range(1,altura+1,2):
#     for j in range(i,0,-2):
#         print(j,end=" ") # función para imprimir  los valores seguidos en una linea separados por un espacio
#     print("")
    
""" Programa que pide al usuario una palabra y luego muestra una a una las letras
de la palabra introducida empezando por la última.
"""
# palabra = input('digite una palabra: ')

# for i in range(len(palabra)-1, -1, -1):
#     print(palabra[i])

""" Programa en el que se pregunta al usuario por una frase y una letra, y
se muestra por pantalla el número de veces que aparece la letra en la frase.
"""
# frase = input('digite una frase: ')
# letra = input('escoja una letra: ')

# cantidad = 0

# for i in frase:
#     if i == letra:
#         cantidad +=1
# print(f'la letra {letra} se repite {cantidad} veces.')
