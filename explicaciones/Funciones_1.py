"""
    Script para explicar funciones en Python.

"""


""" 1. Definición básica. """

def buenosdias(nombre):
    """Esta función  le desea buenos días a una persona.
        
        Parameters:
        nombre : String con nombre de persona

        Return:
        None
    """
    print("Buenos días!, ",  nombre )


"""2. Llamado"""

minombre = "Superman López"
buenosdias(minombre) #Agumentos


"""3. Return

La declaración return se usa para salir de una función y volver al lugar desde donde se llamó.
Esta declaración puede contener expresiones que se evalúan y devuelven un valor. 
Si no hay expresión en la declaración o la declaración de retorno en sí no está presente dentro de una función,
entonces la función devolverá el objeto None.

Python Doc: The None keyword is used to define a null."""

minombre = "Rigoberto"
print(buenosdias(minombre))


def buenasnoches(nombre):
    """Esta función  le desea buenas noches a una persona.
        
        Parameters:
        nombre : String con nombre de persona

        Return:
         String -Es hora de descansar-
    """
    print("Buenas noches!, ",  nombre )

    return "Es hora de descansar"

minombre = "Rigoberto"
print(buenasnoches(minombre))




def valor_absoluto(num):
    """Esta función retorna el valor absoluto
    de un número real.

        Parameters:
        num : Float

        Return:
         num : Float con valor absoluto 
    
    """
    if num >= 0:
        return num
    else:
        return -num

print(valor_absoluto(-120.03))

"""4. Alcance y yiempo de vida de las variables

El alcance de una variable es la parte de un programa donde se reconoce la variable. 
Los parámetros y variables definidos dentro de una función no son visibles desde el exterior. 
Por lo tanto, tienen un alcance local.

El tiempo de vida de una variable es el período durante el cual la variable esta referenciada en memoria. 
El tiempo de vida de una variable dentro de una función es tan larga como la ejecución de la función."""


def funcion_prueba():
    """Esta función sirve para explicar el alcance y tiempo de vida de una variable
        en una función.
    """
    variable = 1230
    print("Valor dentro de la función:",variable)

variable = 3450
funcion_prueba()
print("Valor fuera de la función:",variable)

## Revisar en http://www.pythontutor.com/visualize.html#mode=edit

"""1. Considere la siguiente función"""

def suma_lista(lista):
    """Esta función  suma los números de una lista
        
        Parameters:
        lista : Lista con números

        Return:
        suma: suma de los elementos de la lista
    """
    suma = 0
    for elem in lista:
        suma += elem
    return suma

milista = [12.5,10,13.4,13.22,7,2.34]
print(suma_lista(milista)) # En este llamado el argumento es milista y es OBLIGATORIO

"""Que pasa si no envio el argumento"""

# suma_lista()

"""2. Valores por defecto"""

def suma_lista2(lista = [1,2,3]):
    """Esta función  suma los números de una lista
    La diferencia con la anterior función es que en esta el parametro lista
    tiene un valor por defecto, por lo tanto cuando llamemos a esta función
    los argumentos son opcionales.
        
        Parameters:
        lista : Lista con números

        Return:
        suma: suma de los elementos de la lista
    """
    suma = 0
    for elem in lista:
        suma += elem
    return suma

milista = [12.5,10,13.4,13.22,7,2.34]
print(suma_lista2(milista)) # Con argumento
print(suma_lista2()) #Sin argumento, ahora si se puede pq hay un valor por defecto en la definición del parametro.

""" 3. Funciones definidas con multiples parametros/LLamados con multiples argumentos"""

def elimina_caracteres(texto,eliminar = ["a","e","i","o","u"]):
    """Esta función elimina de un texto un conjunto de caracteres.
        
        Parameters:
        texto : String con texto del cual se quiere eliminar caracteres
        eliminar: Lista con los caracteres que quiero eliminar.

        Return:
        textopro: Texto sin los caracteres que se especificaron.
    """
    textopro = ""
    for caracter in texto:
        if caracter not in eliminar:
            textopro = textopro + caracter
    return textopro

mi_texto = "Colombia"

print(elimina_caracteres(mi_texto)) # Un solo argumento

print(elimina_caracteres(mi_texto,["l"])) # Multiples argumentos asignados por posición!!!

"""4. Python definición de argumentos por palabra clave"""

result1 = elimina_caracteres(texto=mi_texto, eliminar=["l"]) # Todos los argumentos deben ir definidos por palabra clave
result2 = elimina_caracteres(eliminar=["l"],texto=mi_texto) # Diferente orden

print(result1, " ", result2)

# elimina_caracteres(texto=mi_texto,["l"]) # Error