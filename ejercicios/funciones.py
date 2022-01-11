# def saludo(nombre):
#     """ función que pide el nombre del usuario y muestra por pantalla el saludo
#     ¡Hola amig@! + nombre digitado.
#     """
#     print(f'¡Hola amig@! {nombre}')
    
# name = input('digite su nombre: ').capitalize()
# saludo(name)

# def media(lista):
#     """ Función que recibe una muestra de números en una lista y devuelve su media.
#     """
#     suma = 0
#     for i in lista:
#         suma += i
#     cantidad = len(lista)
#     promedio = suma / cantidad
#     return promedio

# listado = [5, 6, 4, 3, 7, 5, 8.2, 9.3, 7.45, 76.8]
# promedio = media(listado)
# print(f'la media de la lista es: ', promedio)


# def iva(cantidad, iva = 1.19):
#     """ Función que calcula el total de una factura tras aplicarle el IVA. La función
#     debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total
#     de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar
#     un 19%.
#     """
#     total = cantidad * iva
#     return total

# producto = float(input('ingrese el precio del producto: '))
# impuesto = float(input('ingrese el iva del producto: '))

# if impuesto <= 0:
#     total = iva(producto)
# else:
#     total = iva(producto, impuesto)

# print(f'el precio del producto es: {producto}\nel impuesto es de {impuesto}%\ny el total de la factura es: {total}')

# def divisores(num):
#     """ Función que calcula los divisores de un número"""
#     lista = []
#     div = 1
#     for i in range(num):
#         if num % div == 0:
#             lista.append(div)
#         div += 1
#     return lista

# def mcd(numero_1, numero_2):
#     """función que calcula el máximo común divisor de dos números.
#     """
#     div1 = divisores(numero_1)
#     div2 = divisores(numero_2)
#     total = []
#     for i in div1:
#         if i in div2:
#             total.append(i)
#     mcdiv = max(total)
#     return mcdiv

# num_1 = int(input('ingrese el primer número: '))
# num_2 = int(input('ingrese el segundo número: '))
# divisor = mcd(num_1, num_2)
# print(f'el máximo común divisor entre {num_1} y {num_2} es {divisor}')

# def mcm(num_1,num_2):
#     """función que calcula el mínimo común múltiplo de dos números
#     """
#     mult = []
#     mult.append(num_1)
#     mult.append(num_2)
#     maxi = max(mult)
#     multi1 = []
#     multi2 = []
#     multiplicar = 1
#     for i in range(maxi):
#         multiplo = num_1 * multiplicar
#         multiplos = num_2 * multiplicar
#         multi1.append(multiplo)
#         multi2.append(multiplos)
#         multiplicar += 1
    
#     total = []
#     for i in multi1:
#         if i in multi2:
#             total.append(i)
#     mincm = min(total)
#     return mincm

# num1 = int(input('Digite un número: '))
# num2 = int(input('Digite otro número: '))
# minimo = mcm(num1, num2)
# print(f'el mínimo común múltiplo entre {num1} y {num2} es {minimo}')

# def area(radio):
#     """ Función que calcula el area de un círculo
#     """
#     import math
#     circulo = round((math.pi)*(math.pow(radio,2)),2)
#     return circulo

# def volumen(rad,altura):
#     """ Función que calcula el volumen de un cilindro
#     """
#     circulo = area(rad)
#     cilindro = circulo * altura
#     return cilindro

# radio = float(input('Digite el radio de la base del cilindro: '))
# altura = float(input('Digite la altura del cilindro: '))
# ar = area(radio)
# total = volumen(radio,altura)
# print(f'El area del circulo con radio {radio} es: {ar}')
# print(f'El volumen del cilindro con altura {altura} es: {total}')

def grande(numero):
    """ Función que calcula cual es el número más grande que se puede formar
    con las cifras de un número de 4 dígitos
    """
    orden = "".join(sorted(numero,reverse=True))
    return orden

def peque(numero):
    """ Función que calcula cual es el número más pequeño que se puede formar
    con las cifras de un número de 4 dígitos
    """
    

numero = input('digite un número de 4 cifras: ')
orden = grande(numero)
print(orden)