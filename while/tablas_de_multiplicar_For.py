# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:41:27 2021

@author: Pipe
"""
import re

# print('3 ® 0 = ' + str(3*0))
# print('3 x 1 = ' + str(3*1))
# print('3 x 2 = ' + str(3*2))
# print('3 x 3 = ' + str(3*3))
# print('3 x 4 = ' + str(3*4))
# print('3 x 5 = ' + str(3*5))
# print('3 x 6 = ' + str(3*6))
# print('3 x 7 = ' + str(3*7))
# print('3 x 8 = ' + str(3*8))
# print('3 x 9 = ' + str(3*9))
# print('3 x 10 = ' + str(3*10))



Tabla = int(input('¿Qué tabla quiere que escriba? '))
print('La tabla que selecciono se escribirá máximo hasta el 20')
print('Las tablas del 0 al 10 avisarán que son las que aprenden los niños')
Lim = int(input('¿Hasta qué número quiere que escriba la tabla? '))

for i in range(0,Lim+1):
    Mult = Tabla * i
    print(str(Tabla) + ' ® ' + str(i) + ' = ' + str(Mult))
    if i >= 20:
        break
    if i > 10:
        continue
    print('Tabla para niños')


# Programa para escribir las tablas del 1 al 9

for Tabla in range(1,10):
    print('Tabla del ', Tabla)
    for i in range(0,10):
        Mult = Tabla * i
        print(str(Tabla) + ' ® ' + str(i) + ' = ' + str(Mult))
 
    
if True:
    print('Hola Mundo')
    
while True:
    print('Hola Mundo')
    continue
    print('Hola Marte')
    
# for j in range(0,30,3):
#     print(j)
    
