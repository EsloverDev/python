#función para determinar el nombre del producto con mayor precio
def precio_mayor(tienda):    
    mayor = list(tienda.keys())[0]
    for i in tienda:
        if tienda[i][1] > tienda[mayor][1]:
            mayor = i
    return tienda[mayor][0]  

#función para determinar el nombre del producto con menor precio
def precio_menor(tienda):    
    menor = list(tienda.keys())[0]
    for i in tienda:
        if tienda[i][1] < tienda[menor][1]:
            menor = i
    return tienda[menor][0]

#función para calcular el promedio de precios
def promedio_precios(tienda):    
    promedio = 0
    for i in tienda:
        promedio += tienda[i][1]
    promedio /= len(tienda)    
    return promedio  

#función para calcular el valor del inventario
def valor_inventario(tienda):    
    valor_inventario = 0.0
    for i in tienda:
        valor_inventario += tienda[i][1] * tienda[i][2] 
    return valor_inventario  

#función para realizar una actualización de productos en la base de datos
def actualizar_producto(tienda,producto):
    global error
    if producto[0] in tienda:
        codigo = producto[0]
        producto.pop(0)
        tienda[codigo]=producto
        return tienda
    else:
      error = True
      return error

#función para eliminar un producto de la base de datos
def borrar_producto(tienda,producto):
    global error
    if producto[0] in tienda:
        tienda.pop(producto[0])
        return tienda
    else:
      error = True
      return error

#función para agregar un producto a la base de datos    
def agregar_producto(tienda,producto):
    global error
    if producto[0] in tienda:
        error = True
        return error
    else:
        codigo=producto[0]
        producto.pop(0)
        tienda[codigo]=producto
        return tienda

#función para capturar los datos la información del producto a modificar
def leer_datos():
  operacion=input()
  producto=input().split    () # ['11', 'papa','3500.5','45']----> 11:['papa',3500.5,45]
  producto[0]=int(producto[0])
  producto[2]=float(producto[2])
  producto[3]=int(producto[3])

  return operacion, producto

#función para crear la base de datos
def productos():
    tienda ={1:['Tangelos',9000.0,67],
          2:['Limones',2500.0,35],
          3:['Peras',2700.0,65],
          4:['Arandanos',9300.0,34],
          5:['Tomates',8100.0,42],
          6:['Fresas',9100.0,90],
          7:['Helado',4500.0,41],
          8:['Galletas',700.0,18],
          9:['Chocolates',4500.0,80],
          10:['Jamon',11000.0,55]}
    return tienda

"""Se desea crear un programa que permita Agregar, Borrar y Acualizar
productos a la base de datos, si este proceso se puede desarrollar correctamente
deberá entonces calcular e imprimir el nombre del producto con mayor y menor precio,
el promedio de los precios de los productos y el valor total del inventario,
si no, deberá imprimir un mensaje de error"""

global error
#Desarrollo parte 1: Programa para modificar la base de datos
tienda = productos() #Crear la base de datos
error = False # Creamos una bandera con la que evaluaremos si se genera o no un error en las operaciones
operacion,producto = leer_datos() #Solicitamos la información de los productos a modificar y el proceso a ejecutar

#Ejecución del proceso seleccionado por el usuario
if operacion=='AGREGAR':
    tienda = agregar_producto(tienda,producto)
elif operacion=='BORRAR':
    tienda = borrar_producto(tienda,producto)
elif operacion=='ACTUALIZAR':
    tienda = actualizar_producto(tienda,producto)

#Desarrollo de la parte 2: Generar una impresión de acuerdo con el estado de error
#Mediante el if determinaremos el estado de error, si es verdadera se ejecutaran las instruccciones
#identadas al if y si si es falsa se ejecutaran las instrucciones identadas al else
if error: #Si error es verdadera, se debe imprimir un mensaje de ERROR 
    print("ERROR") 
else: # Si no es verdadera, se debe continuar con la impresión de los cuatro valores solicitados
    nombre_mayor = precio_mayor(tienda)
    nombre_menor = precio_menor(tienda)
    promedio = promedio_precios(tienda)
    inventario = valor_inventario(tienda)
    print(nombre_mayor, nombre_menor, round(promedio,1), round(inventario,1))






