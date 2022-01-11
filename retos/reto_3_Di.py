def import_datos():
  for i in range(int(input())):
    datos = []
    datos_prueba = [int (i) for i in input().split()]
    datos.append(datos_prueba)
    return datos

def verificacion_veh(datos):
    veh_apto = []
    for i in range(len(datos)):
      if (datos[i][0]<=2005 and datos[i][1]<=950 and datos[i][2]>=702 and datos[i][3]<=1600):
        veh_apto.append(datos[i][4])

    if len(veh_apto)==0:
      print("NO DISPONIBLE")
    else:
      for i in veh_apto:
        print([i])

datos = import_datos()
verificacion_veh(datos)