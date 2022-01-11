"""
Programa para explicar variables/asignaciones y operadores básicos en Python.
Herramienta interesante: http://pythontutor.com/
Nota: El código aquí presentado presenta errores!!, el proposito de este script es totalmente pedagógico. 

"""

## 1. Crear una variable y asignarle un valor
number = 5  # = es un operador de asignación
print(number)
# Ahora cambiemos el valor de la variable
number = 10
print(number)
# Tipo inferido automáticamente
print(type(number))

## 2. Tipado dinámico
number = "Ahora soy un string"
print(type(number))

## 3. Asignación de variables multiples
a, b, c = 5, 3.2, "Hello"
print(a)
print(b)
print(c)

## 4. Convenciones para el nombramiento de variables
# - No usar simbolos especiales !, @, #, $, %, etc. 
# - No inicie el nombre con un número digito.
# - Los nombres de variables deben tener una combinación de letras en minúsculas (a a z), mayúsculas (A a Z) 
# , dígitos (0 a 9) o un guión bajo (_). 
# - Nombres con sentido.!!
nombre_persona_1 = "Manuel"
nombre_persona_2 = "Enrique"
nombrePersona_1 = "Francisco"

# No usar palabras reservadas: as. assert. break. class. continue. def. del. elif. else. except. exec. finally. for.
# from. global. if. import. in. is. lambda. not. or. pass. print. raise. return. try. while. with. yield.

## 5. Operadores aritméticos basicos
numero_1 = 7
numero_2 = 2

#suma
print(numero_1 + numero_2)
suma = numero_1 + numero_2
print(suma)

#resta
resta = numero_2 - numero_1
print(resta)

#negacion
neg_resta = -resta
print(neg_resta)

#División
divi = numero_1/numero_2
print(divi)

#Exponente
expo = numero_1 ** numero_2
print(expo)

#Módulo
modulo = numero_1 % numero_2
print(modulo)

cociente = numero_1 // numero_2
print(cociente)

#Que pasa si opero una cadena de caracteres y un numero
10 + "a" #Error de type

## 6. Existe un orden de precedencia de los operadores.
# - Exponente: **
# - Negación: -
# - Multiplicación, División, Módulo: *, /, %
# - Suma, Resta: +, 

operacion = -numero_2 ** 2 + numero_1/7
print(operacion)

## 7. Operadores de asignación
# += El operador += suma a la variable del lado izquierdo el valor del lado derecho.
numero_1 += 2 # Es equivalente a numero_1 = numero_1 + 2
print(numero_1)

# -= El operador -= resta a la variable del lado izquierdo el valor del lado derecho.
numero_1 -= 3
print(numero_1)

# *= El operador *= multiplica a la variable del lado izquierdo el valor del lado derecho
numero_1 *= 2
print(numero_1)

# **= , /=, %= son operadores de asignación para la exponeciación, división y modulo respectivamente.

## 8. Operadores relacionales. Evaluan expresiones de verdad.

# == El operador == evalua que los valores sean iguales.
5 == 3
5 == 5
verdad = 4==3
print(verdad)
"Amigo" == 5
type("Amigo") == str

# != El operador != evalua si los valores son distintos.
5 != 3
5 != 5

# Operadores de comparación <,>,<=,>=
5 < 3
5 > 3
5 <= 3
5 >= 3

## 9. Volviendo a las listas, diccionarios, tuplas y set. Revisar en py tutor.
mivar = "Hola Mundo!"
milista = [12,"a",True,"b",5, mivar]
print(milista[0]) #acceso al primer elemento de la lista - index 0
print(milista[5]) #acceso al segundo elemento de la lista - index 1
nueva_milista = milista[0:2] #acceso a los dos primeros elementos de la lista obj[start:stop]
print(nueva_milista) 
#Que pasa si trato de acceder al index 6?
milista[6]
#Las listas son mutables, las puedo cambiar!
milista[0] += 12
print(milista)


midiccionario = {"1":"Hola","2":"Mundo","3":"Soy yo","4":"!"}
print(midiccionario["1"])
print(midiccionario["4"])
# Que pasa si llamo a la llave "5"?
midiccionario["5"]

#Las llaves en los diccionarios tambien pueden ser enteros.
midiccionario_2 = {1:"Hola",2:"Mundo","3":"Soy yo",4:"!"}
print(midiccionario_2[1])
print(midiccionario_2[2])
print(midiccionario_2["3"])
print(midiccionario_2[3]) #Error de llave.

## 10. Un error final
# Llamar variables no declaradas genera un NameError
# print(noExiste)
# hh + jj