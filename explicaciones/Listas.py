"""Script con ejemplos sobre listas"""
#Definicion basica
l = [1, 3, -0.5, True, 'Patilla']
print( l[2] )
l[0] = l[0] + 1 #Modificamos que valor?
print(l[0]) #Que valor nos va a imprimir

"""En Python las tuplas se diferencian de las listas porque se definen con () 
 y son inmodificables """

t = (1, 3, -0.5, True, 'Patilla')
print( t[2] )
# t[0] = t[0] + 1 # ERROR: una tupla no se puede modificar

""" Diccionarios:  Colleción no-ordenada de pares llave-valor"""
agenda = {'Ana':644343434, 'Edu':622121243, 'Bob':679444444} 
print( agenda['Edu'] ) 
agenda['Pep'] = 686252554 #para agregar llaves y valores al diccionario

""" Ejemplo 
{"Llave1":'valor de la llave 1','Llave2': "valor de la llave 2"} """
{"Llave1":0,'Llave2': 2}
type({"Llave1":0,'Llave2': 2})

"""RECORRER LISTAS
1 CON FOR ENTRANDO DIRECTAMENTE A LA LISTA"""

frutas=["pera", "manzana", "mandarina","uvas"]

for e in frutas:
    print(e)

"""2 Encontrando el tamaño de la lista y recorriendola con rango"""

for i in range(len(frutas)):
    print (frutas[i])

"""SLICES """
a = ['Mary', 'gorro', 'a', 'pequeño', 'niño']
b = a[1:4]          # b vale ['gorro', 'a', 'pequeño']
b = a[2: ]          # b vale ['a', 'pequeño', 'niño']
b = a[ :3]          # b vale ['Mary', 'gorro', 'a']
b = a[-4:-2]        # b vale ['gorro', 'a']
del a[1:4:2]        # a vale ['Mary', 'a', 'niño']
# B=a[-4:-6:-1]
# print(B)

"""FUNCIONES sobre listas"""
# len( lista )            # devuelve el número de elementos
# [ lista1 ] + [ lista2 ] # concatena listas
# [ valor ] * num         # crea lista de num veces valor
# elemento in lista       # Cierto/Falso que lista contiene el elemento
# lista.append(elemento)  # añade elemento al final
# lista.clear() # vacía la lista
# lista.copy() # lista nueva con los mismos elementos
# lista.count(elemento) # número de apariciones del elemento
# lista1.extend(lista2) # añade a lista1 los elementos de lista2
# lista.index(elemento) # índice de 1ª aparición del elemento
# lista.insert(índx, elem) # inserta elemento en la posición del índice
# lista.pop(índice) # borra elemento en la posición del índice
# lista.remove(element) # borra las apariciones del elemento

"""Generadores de listas:"""

ll = [ x**2 for x in range(100) if x%2 == 0 ]

"""Seria una manera breve de hacer:"""

ll = []
for x in range(100):
 if x%2 == 0:
    ll.append( x**2 )

#Para inicializar rápidamente una lista a un valor, mejor utilizar el operador *:

 ll = 100*[0] # lista de 100 ceros

 """En python se manejan string o cadenas de caracteres, se recorren de la misma manera 
 que recorremos las listas, lineas 24 a 33
 Ejemplo"""

letraNIF = 'TRWAGMYFPDXBNJZSQVHLCKE'
for A in letraNIF:
    print (A)

"""En Python, los caracteres que forman el string están codificados en Unicode.
En Python los strings son inmutables, es decir, que no podemos modificar sus caracteres.

Funciones sobre strings:
Sobre cadenas de caracteres podemos utilizar la mayoría de las funciones que ya utilizamos
sobre listas, pero además algunas funciones específicas de strings. Aquí va un resumen de las que
considero más importantes:"""

s="Hola como estas"
# len( s )                # devuelve el número de caracteres de s
# s1 + s2                 # concatena strings s1 y s2
# s2 in s                 # cierto/falso que s contiene s2
# s.lower() y s.upper()   # pasa la cadena s a minúsculas o mayúsculas
# s.startswith(s2)        # indica si la cadena comienza con s2
# s.endswith(s2)          # indica si la cadena acaba con s2
# s.find(s2)              # índice de 1ª aparición de s2 en s
# s.count(s2)             # número de apariciones de s2 en s
# s.replace(s2, s3)       # reemplaza en s las apariciones de s2 con s3
# s.strip()               # elimina de s espacios iniciales y finales
# s.split(s2)             # divide s en trozos, separando con s2
# s.join(l)               # cadena con elementos de lista l sep. por s
# s.isalnum()             # cierto/falso que s es letra o número
# s.isalpha()             # cierto/falso que s es letra
# s.isdecimal()           # cierto/falso que s es número
# s.isspace()             # cierto/falso que s es un separador
# s.isprintable()         # cierto/falso que s es símbolo representable
# s.islower() , s.isupper() # cierto/falso que s es minúscula/mayúscula
