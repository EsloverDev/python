# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:39:43 2021

@author: Pipe
"""

# Programa para calcular el promedio de las notas de un estudiante

print('Bienvenido Profesor, este programa le ayuda a calcular el promedio de las notas de sus estudiantes')

ListaNota = []
CantidadNotas = 1
Continuar = True
# Suma = 0
while Continuar:
    # Suma = Suma + float(input('Introduzca la nota ' + str(CantidadNotas)))
    ListaNota.append(input('Introduzca la nota ' + str(CantidadNotas) + ' '))
    Deseo = input('¿Desea continuar con mas notas? (si/no)')
    if Deseo == 'si':
        CantidadNotas = CantidadNotas + 1
    else:
        Continuar = False

Suma = 0
for Nota in ListaNota:
    Nota = float(Nota)
    Suma += Nota

Promedio = Suma/CantidadNotas

print('El promedio de las notas es: ', Promedio)
input()



