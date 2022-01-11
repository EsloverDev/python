def leer_datos():
    operacion = input()
    producto= input().split()
    producto[0]= int(producto[0])
    producto[2]= float(producto[0])
    producto[3]= int(producto[0])

    return operacion, producto

def agregar_producto(tienda,producto:list):
    
    if producto[0] in tienda:
        print("ERROR")
    else:
        codigo= producto[0]
        producto.pop(0)
        tienda[codigo]= producto
        print(tienda)

def borrar_producto(tienda:dict,producto:list):
    if producto[0] in tienda:
        tienda.pop[0]
        print(tienda)
    else:
        print('ERROR')

def actualizar_producto(tienda:dict,producto:list):
    if producto[0] in tienda:
        codigo= producto[0]
        producto.pop(0)
        tienda[codigo]= producto
        print(tienda)
    else:
        print('ERROR')
def productos():
    tienda = {1: ['Tangelos',9000.0, 67],
    2:['Limones', 2500.0, 35],
    3:['Peras', 2700.0, 65],
    4:['Arandanos', 9300.0, 41],
    5:['Tomates', 8100.0, 42],
    6:['Fresas', 9100.0, 90],
    7:['Helado', 4500.0, 41],
    8:['Galletas', 700.0,18],
    9:['Chocolate', 4500.0,80],
    10:['Jamon', 11000.0,55]
    }

    operacion, producto= leer_datos()

    if operacion == 'AGREGAR':
        agregar_producto(tienda,producto)

    elif operacion == 'BORRAR':
        borrar_producto(tienda, producto)

    elif operacion == 'ACTUALIZAR':
        actualizar_producto(tienda,producto)

productos()