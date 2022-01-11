def leer_datos():
    n, k = input().split()
    notas = [int(x) for x in list(input().split())]
    return (int(n),int(k),notas)

# 1 2 3 1 2
def copias_totales(k,notas):
    c_totales = 0
    if notas.count(notas[0])==len(notas):
        c_totales=len(notas)-1
    else:
        ya_evaluados=[]
        for i in notas:
            if (i not in ya_evaluados):
                ya_evaluados.append(i)
                contador=0
                contador=notas.count(i)
                if (contador>1):
                    contador=contador-1
                    c_totales+=contador

    return c_totales
    
def copias_detectadas(k,notas):
  c_detectadas=0
  if notas.count(notas[0])==len(notas):
    c_detectadas=len(notas)-1
  else:

      for i in range(k, len(notas)):  # 3 4
            li = i-k
            x = notas[li:i-1]  # [1 2 3] --> [2 3 1]
            if (notas[i] in x):
                c_detectadas += 1
                
  return c_detectadas

N,k,notas=leer_datos()
print(copias_totales(k,notas),copias_detectadas(k,notas))