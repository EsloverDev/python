"""
    Script que explica los ciclos While.
    Estructura:

    while condicion:
        
"""
# 1. Estructura basica

i = 1
while i <= 3:
    print(i)
    i += 1 # i=i+1 suma 1 a la variable i


# 2. Acumulador ahora con ciclo while
n = 10
sum = 0 #acumulador
i = 1 #Contador

while i <= n:
    sum = sum + i
    i += 1    # Contador, OJO se debe actualizar para que la condición sea falsa en algún momento.

print("The sum is {}". format(sum))

# 3. Cuidado con los bucles infinitos

#i = 1
#while i <= 50:
#    print(i) #Nunca se actualiza i, por lo tanto siempre va ser menor a 50

i = 1
while i <= 50:
    print(i)
    i *= 5
print("Programa terminado")


# 4. Ciclos While útiles para mantener la ejecución de un programa hasta un input del usuario

# numero = int(input("Escribir número positivo: "))
# while numero < 0:
#    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
#    numero = int(input("Escriba un número positivo: "))
# print("Por fin escribio un número positivo")


# 5. Prediga (Prueba de escritorio) que se va desplegar en consola.
print("Ejercicio")
n = 10
while n > 0 :
    n -= 1 # n=n-1
    if n == 5:
        print(n)
print(n)