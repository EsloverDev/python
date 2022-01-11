"""
    Script para explicar modulos.

   Podemos importar las definiciones dentro de un módulo a otro módulo con "import".

"""

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