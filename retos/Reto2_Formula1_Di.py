distancia_camara, record_actual, tiempo_trayecto = input().split()

distancia_camara = float(distancia_camara)
record_actual = float(record_actual)
tiempo_trayecto = float(tiempo_trayecto)

vel_media = (distancia_camara/1000) / (tiempo_trayecto/3600)

if distancia_camara < 0 or record_actual < 0 or tiempo_trayecto < 0:
  print("VALORES NEGATIVOS")
elif vel_media > record_actual and vel_media < (record_actual*1.25):
  print("NUEVO RECORD")
elif vel_media > (record_actual*1.25):
  print("ENTREVISTA")
else: 
  print("VELOCIDAD NORMAL")







