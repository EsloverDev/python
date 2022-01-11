"""
    Script para explicar el manejo de excepciones en Python
"""
#Dcumentacion sobre excepciones: https://docs.python.org/3/library/exceptions.html
import sys

# 1. Try-except

def reciproco(milista):
    """Retorna el reciproco de cada numero de una lista de numeros.
    Parametros:
    milista: Lista de numeros
    Retorna:
    Lista con los reciprocos
    """
    for num in milista:
        try:
            print("Número:", num)
            r = 1/num
            print("El reciproco de {}, es: {}".format(num,r))
        except:
            print("Oops!",sys.exc_info()[0]," ocurrio.")

milistaNumeros = [3, 0, "a", 4 ,5]
reciproco(milistaNumeros)

# 2. Filtrando por tipo de excepción
#En el ejemplo anterior, no mencionamos ninguna excepción en la cláusula except.
#Esta no es una buena práctica de programación, ya que detectará todas las excepciones y manejará todos los casos 
#de la misma manera. Podemos especificar qué excepciones capturará una cláusula except.

def reciproco2(milista):
    """Retorna el reciproco de cada numero de una lista de numeros.
    Parametros:
    milista: Lista de numeros
    Retorna:
    Lista con los reciprocos
    """
    for num in milista:
        try:
            print("Número:", num)
            r = 1/num
            print("El reciproco de {}, es: {}".format(num,r))
        except TypeError:
            print("La división se realiza entre números")
        except ZeroDivisionError:
            print("Las divisiones por cero no estan permitidas")
        except:
            pass #Operación núla, nada sucede

reciproco2(milistaNumeros)

# 3. Multiples excepciones en un mismo except.

def reciproco3(milista):
    """Retorna el reciproco de cada numero de una lista de numeros.
    Parametros:
    milista: Lista de numeros
    Retorna:
    Lista con los reciprocos
    """
    for num in milista:
        try:
            print("Número:", num)
            r = 1/num
            print("El reciproco de {}, es: {}".format(num,r))
        except (TypeError,ZeroDivisionError):
            print("Error de tipo de dato o de divsión por zero")
        except:
            pass #Operación núla, nada sucede

reciproco3(milistaNumeros)

#4. Levantando excepciones
# En Python, se generan excepciones cuando se producen los errores correspondientes en tiempo de ejecución.
# Nosotros tambien podemos levantar de forma forzada las excepciones utilizando la palabra clave raise.
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)


#5. Excepciones personalizadas
# En ocasiones, es posible que necesite crear excepciones personalizadas que sirvan a su propósito.
# En Python, los usuarios pueden definir tales excepciones creando una nueva clase. 
# Esta clase de excepción debe derivarse, directa o indirectamente, de la clase Excepción. 

class ErrorValorMuyPeque(Exception):
   """Raised when the input value is too small"""
   pass

numero = 10

while True:
    try:
        num_usuario = int(input("Ingrese un número: "))
        if num_usuario < numero:
            raise ErrorValorMuyPeque
        break
    except ErrorValorMuyPeque:
        print("Este valor es muy pequeño!")