"""
    Script que explica la estructura de seleccion if/else.

"""
#import math

#1. Estructura básica

if 5==5:
    print("Soy parte del bloque de instrucciones del if")
    print("Me despliego en consoloa por lo tanto la condición es cierta")



#Notese la identación/sangrado, se recomienda utilizar sangrado. 
#Este término significa mover un bloque de texto hacia la derecha insertando espacios o tabuladores, 
#para así separarlo del margen izquierdo y mejor distinguirlo del texto adyacente.

#En python los bloques de código van definidos por su sangrado!!!

if 5!=5:
    print("NO me despliego en consola por lo tanto la condición no se cumple")
print("Yo no estoy dentro del bloque de instrucciones del if")

#Otros operadores y condiciones con variable
num = 3
if num > 0:
    print(num, "es un número positivo")

num = -1
if num > 0:
    print(num, "es un número positivo")
print("Esto siempre se va imprimir, esta por fuera del bloque de instrucciones del if")


# 2. Si/Entonces, If/Else

#num = 50
num = -100
#num = 0

if num >= 0:
    print("Número positivo o cero")
else:
    print("Número Negativo")
print("Hola siempre me imprimo")


# 3. Chequeo multiple. if/elif/else

num = 0

if num > 0:
    print("Número positivo")
elif num == 0:
    print("Cero")
else:
    print("Número negativo")


# Ejemplo sencillo

edad = 11
if edad >= 18:
    print("Usted es mayor de edad")
elif edad < 0:
    print("Error!, edad negativa")
else:
    print("Usted es menor de edad")

# 4. Operadores lógicos
# Operadores de comparación: ==, !=, <, >, <=, >= (numeros, strings)
# Operadores booleanos -> permiten escribir expresiones booleanas (solo BOOL) . ==, != (XOR) ,AND, OR, NOT

# Ejercicio: (x ∧ y) ∨ ¬z
x = False
y = False
z = False
#Revisar tablas de verdad 
res = (x and y) or not z
print("Si x es {}, y es {}, y z es {}, la expresión (x ∧ y) ∨ ¬z es {}".format(x,y,z,res))

# Operadores booleanos en la practica
edad = 12
if edad < 0:
    print("No se puede tener una edad negativa")
elif edad >= 0 and edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")

# Prediga el bloque que se va a ejecutar.
numero = 16

if numero % 2 == 0 and numero % 4 != 0:
    print("{} es múltiplo de dos".format(numero))
elif numero % 4 == 0:
    print("{} es múltiplo de cuatro y de dos".format(numero))
else:
    print("{} no es múltiplo de dos".format(numero))




# Diga el bloque que se va a ejecutar y el valor resultante de número

numero = 15

if numero >= 5 and numero < 18:
    numero +=  10
elif numero < 5 or numero >18:
    numero *= 2
else:
    print("Con que valor númerico se ejecuta este print?")

print("El valor de la variable número es {}".format(numero))

# 5. Evaluando membresías en colecciones
# in, not in

vocales = ["a","e","i","o"]

if "a" in vocales:
    print("La vocal 'a' esta en vocales")

if "u" not in vocales:
    print("La vocal 'u' no esta en vocales")

texto="Hola mundo, aquí voy!"
if "Hola" in texto:
    print("Hola esta en el string")


# 6. Anidación de if

num = -12
if num >= 0:
    if num == 0:
        print("Cero")
    else:
        print("Número Positivo")
else:
    print("Número Negativo")

# Prediga las funciones print que se van a ejecutar

var = 200
if var < 200:
    print("Menor que 200")
    if var == 150:
        print("Es 150")
    elif var == 100:
        print("Es 100")
    elif var == 50:
        print("Es 50")
    elif var < 50:
        print("Menor que 50")
    else:
        print("Con que valores me imprimo yo?") #Pregunta interesante.
else:
    print("Mayor o igual a 200")