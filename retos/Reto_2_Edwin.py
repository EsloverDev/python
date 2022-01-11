distancia, velocidad, tiempo = input().split() 

distancia = float(distancia)
velocidad = float(velocidad)
tiempo = float(tiempo)

exceso_1 = velocidad * 1.25

dist_km = distancia / 1000
tiempo_h = tiempo / 3600
velocidad_real = dist_km / tiempo_h

if distancia < 0 or velocidad < 0 or tiempo < 0:
    print("VALORES NEGATIVOS")
elif velocidad_real >velocidad and velocidad_real < exceso_1:
    print("MULTA")
elif velocidad_real > exceso_1:
    print("CURSO SENSIBILIZACION")
else:
    print("OK")