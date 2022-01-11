# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:56:06 2021

@author: Pipe
"""

Condicion = True

if (Condicion):
    print('Hola Mundo')
    
while (Condicion):
    print('Hola Marte')
    Deseo = input('¿Desea continuar? (si/no)')
    if not(Deseo == 'si'):
        Condicion = False
    Jupiter = input('Si desea que salude a Jupiter, escriba "Planeta"')
    if Jupiter != 'Planeta':
        continue
    print('Hola Jupiter')
    