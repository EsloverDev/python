""" Programa que pregunta por una divisa e imprime el símbolo de esa divisa.
"""
# divisas = {'EURO':'€', 'PESOS':'$', 'DOLAR EE.UU':'USD', 'YEN':'¥', 'DOLAR CANADIENSE':'CAD'}
# clave = input('Digite el nombre de una divisa: ')
# clave.upper()
# valor = divisas.get(clave)
# if valor:
#     print(clave,':',valor)
# else:
#     print('No conozco el símbolo de esa divisa.')

""" Programa que pregunta nombre, edad, direccion y telefono, los guarda en un diccionario
y despues los muestra por pantalla
"""
# nombre, edad, direccion, telefono = input('Digite su nombre, edad, direccion y telefono respectivamente separados cada uno por una coma: ').split(',')
# nombre = nombre.upper()
# direccion = direccion.upper()

# agenda = {}
# agenda['name'] = nombre 
# agenda['age'] = edad
# agenda['address'] = direccion
# agenda['phone'] = telefono
# print(agenda['name'], "tiene", agenda['age'], "años, vive en", agenda['address'], "y su número de teléfono es", agenda['phone'],".")

""" Programa que almacena las asignaturas de un curso con sus créditos en un diccionario
y los imprime, también imprime el total de créditos del curso.
"""
# curso = {
#     'Matemáticas' : 6,
#     'Física' : 4,
#     'Química' : 5,
#     'Lenguaje' : 4,
#     'Programación': 7,
#     'Deportes' : 5
#     }

# for i, j in curso.items():
#     print(i, 'tiene:', j, 'créditos')

# total = 0

# for credito in curso.values():
#     total += credito
# # otra forma de recorrer los valores del diccionario
# for credito in curso:
#     total += curso[credito]
# print(f'en total son {total} creditos.')

""" Programa que pregunta por un artículo y su precio, lo añade a un diccionario hasta que
el usuario decida terminar usando la palabra 'FIN'. e imprime la lista de compra y el total.
"""
# articulo = input('Ingrese un artículo: ').capitalize()
# precio = int(input('¿Cúal es el precio del artículo?: '))
# lista = {}
# lista[articulo] = precio

# while True:
#     articulo = input('Ingrese un artículo: ').capitalize()
#     if articulo == 'Fin':
#         break
#     precio = int(input('¿Cúal es el precio del artículo?: '))
#     lista[articulo] = precio

# for key, value in lista.items():
#     print(key, ':', value)

# total = 0
# for i in lista.values():
#     total += i
# print(f'En total son: {total} pesos.')

""" Programa que permite gestionar una base de datos. Los clientes se guardarán en un
diccionario en el que la clave será su NIT, y el valor será otro diccionario con los datos
del cliente (nombre, dirección, teléfono, correo, preferencial), donde preferencial tendrá
el valor True si se trata de un cliente preferencial. El programa debe preguntar al usuario
por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente,
(3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferenciales,
(6) Terminar."""
# base = {}
# while True:
#     print('menú:\n1. Añadir cliente\n2. Eliminar cliente\n3. Mostrar cliente\n4. Listar todos los clientes\n5. Listar clientes preferenciales\n6. Terminar')
#     opcion = int(input('marque una opción: '))
#     if opcion == 1:
#         nit = int(input('digite su NIT: '))
#         datos = {}
#         base[nit] = datos
#         datos['nombre'] = input('¿cuál es su nombre?: ').upper()
#         datos['direccion'] = input('Digite su dirección: ').upper()
#         datos['telefono'] = input('Digite su número de teléfono: ')
#         datos['correo'] = input('Digite su e-mail: ').upper()
#         preferencial = input('¿Ud es cliente preferencial? si/no: ').upper()
#         if preferencial == 'SI':
#             preferencial = True
#         else:
#             preferencial = False
#         datos['preferencial'] = preferencial
#     elif opcion == 2:
#         supr = int(input('Digite el NIT del cliente a eliminar: '))
#         base.pop(supr)
#     elif opcion == 3:
#         ver = int(input('Digite el NIT del cliente que desea ver: '))
#         dat = base.get(ver)
#         if dat:
#             print(ver, ':', dat)
#         else:
#             print(ver, 'no existe')
#     elif opcion == 4:
#         for i, j in base.items():
#             print(i, ':', j['nombre'])
#     elif opcion == 5:
#         for i, j in base.items():
#             if j['preferencial'] == True:
#                 print(i, ':', j['nombre'], 'es un cliente preferencial.')
#     else:
#         print('Gracias por usar nuestros servicios. Hasta luego.')
#         break

""" Programa que implementa sobre un diccionario una agenda formada por nombres de personas
y teléfonos. Dá la opcion de añadir una entrada, modificar una entrada, borrar una entrada
(o avisar si no existía), listar la agenda, y salir. """
# agenda = {}
# while True:
#     print('menú:\n1. Añadir contacto\n2. Modificar contacto\n3. Borrar contacto\n4. Ver agenda\n5. Salir')
#     opcion = int(input('Marque una opción: '))
#     if opcion == 1:
#         nombre = input('Nombre del contacto: ').upper()
#         telefono = input('Digite el número de telefono: ')
#         agenda[nombre] = telefono
#     elif opcion == 2:
#         modificar = input('¿Cuál contacto quiere modificar?: ').upper()
#         telefono = input('Digite el número de telefono: ')
#         agenda[modificar] = telefono
#     elif opcion == 3:
#         borrar = input('Digite el nombre del contacto que va a borrar: ').upper()
#         if borrar in agenda:
#             agenda.pop(borrar)
#         else:
#             print('Éste contacto no existía en tu agenda.')
#     elif opcion == 4:
#         lista = agenda.items()
#         directorio = list(lista)
#         for i in directorio:
#             print(i)
#     else:
#         print('Adiós.')
#         break
