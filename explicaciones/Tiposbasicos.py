""" Programa para explicar los tipos basicos """

# 1. Números Enteros
print(0)
print(1)
print(-14)
print(32424234234) 
type(0)
#Los enteros en Python 3 pueden ser de cualquier tamaño, solo estan limitados por la memoria disponible


#2. Números de punto flotante (reales)
print(1.9)
type(1.9)
print(4e7)
type(4e7)
print(4e-4)
type(4e-4)
# IEEE 754: 64-bit “double-precision” max: 1.8e308
print(1.81e308)


#3. Números complejos <parte real>+<parte imaginaria>j
print(2+3j)
type(2+3j)

#4. Cadenas de caractéres (strings)
print("Yo soy un string") #Comillas dobles (recomendado)
print('Yo tambien soy un string') #Comillas simples
type("Yo soy un string")

# Vamos a generar mi primer error en Python!!
#print('Hola 'mundo', aca estoy! ')
# Alternativa 1: Incluir caracter de escape \ (secuencias de escape)
print('Hola \'mundo\', aca estoy! ')
# Alternativa 2: Intercambiar el delimitador del string
print("Hola 'mundo', aca estoy! ")
#Como imprimo el backslash \?
#print("\")
print("\\")
#Usando triple comillas
print('''Las comillas triples me permiten incluir comillas simples (') y dobles (") sin necesidad del caracter de escape''')


#5. Tipo de dato Booleano
print(True)
type(True)
print(False)
type(False)

#6. Listas. Secuencia ordenada de elementos.
[1, 2.2, 'python']
type([1, 2.2, 'python'])
a = [1, 2.2, 'python']
a[0] # Operador de slicing
a[1]
a[1] = 2.3

#7. Tuplas. Secuencia ordenada "inmutable" de elementos
(5,'program', 1+3j)
type((5,'program', 1+3j))

#8. Set. Secuencia no-ordendad de elementos.
{5,2,3,1,4}
type({5,2,3,1,4})
#No acepta elementos repetidos
{5,2,3,1,1,2,3,4,4}

#Diccionario. Colleción no-ordenada de pares llave-valor
{"Llave1":'valor de la llave 1','Llave2': "valor de la llave 2"}
{"Llave1":0,'Llave2': 2}
print(type({"Llave1":0,'Llave2': 2}))