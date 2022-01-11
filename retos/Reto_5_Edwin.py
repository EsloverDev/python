def precioma(mercado):    
    mayor = list(mercado.keys())[0]
    for i in mercado:
        if mercado[i][1] > mercado[mayor][1]:
            mayor = i
    return mercado[mayor][0]  

def preciome(mercado):    
    menor = list(mercado.keys())[0]
    for i in mercado:
        if mercado[i][1] < mercado[menor][1]:
            menor = i
    return mercado[menor][0]

def promedio_precios(mercado):    
    promedio = 0
    for i in mercado:
        promedio += mercado[i][1]
    promedio /= len(mercado)    
    return promedio

def valor_inventario(mercado):
    valor_inventario = 0.0
    for i in mercado:
        valor_inventario += mercado[i][1] * mercado[i][2]
    return valor_inventario

def actualizar_producto(mercado,producto):
    global error
    if producto[0] in mercado:
        codigo = producto[0]
        producto.pop(0)
        mercado[codigo]=producto
        return mercado
    else:
      error = True
      return error

def borrar_producto(mercado,producto):
    global error
    if producto[0] in mercado:
        mercado.pop(producto[0])
        return mercado
    else:
      error = True
      return error

def agregar_producto(mercado,producto):
    global error
    if producto[0] in mercado:
        error = True
        return error
    else:
        codigo=producto[0]
        producto.pop(0)
        mercado[codigo]=producto
        return mercado

def leer_datos():
  operacion=input()
  producto=input().split()
  producto[0]=int(producto[0])
  producto[2]=float(producto[2])
  producto[3]=int(producto[3])

  return operacion, producto

def productos():
    mercado ={1:['Naranjas',7000.0,35],
          2:['Limones',2500.0,15],
          3:['Peras',2700.0,65],
          4:['Arandanos',9300.0,34],
          5:['Tomates',2100.0,42],
          6:['Fresas',9100.0,20],
          7:['Helado',4500.0,41],
          8:['Galletas',500.0,8],
          9:['Chocolates',4500.0,80],
          10:['Jamon',17000.0,48]}
    return mercado

global error

mercado = productos()
error = False
operacion,producto = leer_datos()

if operacion=='AGREGAR':
    mercado = agregar_producto(mercado,producto)
elif operacion=='BORRAR':
    mercado = borrar_producto(mercado,producto)
elif operacion=='ACTUALIZAR':
    mercado = actualizar_producto(mercado,producto)

if error: 
    print("ERROR") 
else: 
    nombre_mayor = precioma(mercado)
    nombre_menor = preciome(mercado)
    promedio = promedio_precios(mercado)
    inventario = valor_inventario(mercado)
    print(nombre_mayor, nombre_menor, round(promedio,1), round(inventario,1))