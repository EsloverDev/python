n, k = input().split()
n = int(n)
k = int(k)

respuestas = input().split()
copia = {}
detectada = 0
profesor = 0

for i in respuestas:
    if i in copia:
        copia[i] += 1
    else:
        copia[i] = 0

for nota in copia:
    detectada += copia[nota]

for posicion in range(len(respuestas)):
    inicio=posicion-k
    if inicio<0:
        inicio=0
    final=posicion
    if respuestas[posicion] in respuestas[inicio:final]:
        profesor += 1
print(detectada, profesor)
