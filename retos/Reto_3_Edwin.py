numero = int(input())

ahorro = 12000
endeudamiento = 14000
dinero = ahorro + endeudamiento

apto = []
no_apto = []

for i in range(numero):
    cilindrada, año, recorrido, consumo, valor = input().split()
    cilindrada = int(cilindrada)
    año = int(año)
    recorrido = int(recorrido)
    consumo = int(consumo)
    valor = int(valor)
    if cilindrada >= 1200 and cilindrada < 3600 and año >= 2018 and recorrido <= 30000 and consumo < 35 and valor > 13500 and valor <= dinero:
        apto.append(valor)
    else:
        no_apto.append(valor)

if len(apto) != 0:
    for j in apto:
        deuda = j - ahorro
        print(deuda)
else:
    print('NO DISPONIBLE')