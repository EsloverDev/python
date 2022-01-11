def precio_menor(tienda):
    menor_p = tienda [1][1]
    menor_nom = []
    for i in tienda:
        if tienda[i][1] < menor_p:
            menor_p = tienda[i][1]
            menor_nom = tienda[i][0]
    return menor_nom

def precio_mayor(tienda):
    mayor_p = tienda [1][1]
    mayor_nom = []
    for i in tienda:
        if tienda[i][1] > mayor_p:
            mayor_p = tienda[i][1]
            mayor_nom = tienda[i][0]
    return mayor_nom    
    
'''def precio_menor(tienda):
  precios=[] 
  codigos = list(tienda.keys())
  for i in range(1,len(tienda)+1): 
    precios.append(tienda[i][1]) 
  menor = precios[0]  
  nombre_menor=tienda[1][0]
  for i in range(len(precios)): 
    if precios[i] < menor: 
      menor = precios[i]
      nombre_menor=tienda[codigos[i]][0] 
  return nombre_menor

def precio_mayor(tienda):
  precios=[] 
  codigos = list(tienda.keys())
  for i in range(1,len(tienda)+1): 
    precios.append(tienda[i][1]) 
  mayor=precios[0]  
  nombre_mayor=tienda[1][0]
  for i in range(len(precios)): 
    if precios[i] > mayor: 
      mayor = precios[i]
      nombre_mayor=tienda[codigos[i]][0] 
  return nombre_mayor'''

def valor_inventario(tienda):
   valor=0
   for i in tienda:
     valor+=tienda[i][1]*tienda[i][2]
   return valor


def promedio_precios(tienda):
  promedio=0
  for i in tienda:
    promedio+=tienda[i][1]

  promedio= promedio/len(tienda)+1
  return round(promedio,1)

def actualizar_producto(tienda,producto):
  if producto[0] in tienda:
    codigo=producto[0]
    producto.pop(0)
    tienda[codigo]=producto
    print(precio_mayor(tienda),precio_menor(tienda),promedio_precios(tienda),valor_inventario(tienda))
  else:
    print('ERROR')

def borrar_producto(tienda,producto):
  if producto[0] in tienda:
    tienda.pop(producto[0])
    print(precio_mayor(tienda),precio_menor(tienda),promedio_precios(tienda),valor_inventario(tienda))
  else:
    print('ERROR')

def agregar_producto(tienda,producto):
  if producto[0] in tienda:
    print('ERROR')
  else:
    codigo=producto[0]
    producto.pop(0)
    tienda[codigo]=producto
    print(precio_mayor(tienda),precio_menor(tienda),promedio_precios(tienda),valor_inventario(tienda))

def leer_datos():
  operacion=input().upper()
  producto=input().split() 
  producto[0]=int(producto[0])
  producto[2]=float(producto[2])
  producto[3]=int(producto[3])

  return operacion, producto
def productos():
  tienda ={
1 :['Mango',7000.0,99],
2 :['Limones',3600.0,95],
3 :['Peras',2700.0,85],
4 :['Arandanos',8300.0,74],
5 :['Tomates',8400.0,44],
6 :['Fresas',7100.0,99],
7 :['Helado',4400.0,98],
8 :['Galletas',400.0,99],
9 :['Chocolates',4500.0,90],
10 :['Jamon',17000.0,89]
}
  operacion,producto= leer_datos()

  if operacion=='AGREGAR':
    agregar_producto(tienda,producto)
  elif operacion=='BORRAR':
    borrar_producto(tienda,producto)
  elif operacion=='ACTUALIZAR':
    actualizar_producto(tienda,producto)

  
productos()



#min(tienda.values(), key=lambda valor:valor[1])
#promedio_precios(tienda)
#precio_menor(productos)
