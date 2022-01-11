# RETO 4
# 5 2
# 1 2 3 1 2
# c_totales, c_detectadas
# 1 1 1 2 2 2 1   # 1 ---> 5 == cantidad elementos 
def leer_datos():
  N, K = input().split()
  examenes= list(map(int,input().split()))
  return int(N), int(K), examenes


def copias_totales(examenes):
  c_totales=0
  c_totales=len(examenes)-len(set(examenes))
  # if examenes.count(examenes[0])==len(examenes):
  #   c_totales=len(examenes)-1
  # else:
    
  #   # valores = set(examenes)
  #   # print(valores)
  #   # for i in valores:
  #   #   if i in examenes:
  #   #     c_totales += examenes.count(i)-1
 
  return c_totales
# 5 3
# 1 2 3 1 2
def copias_detectadas(examenes,K):
  c_detectadas=0
  for i in examenes:
    if K <= len(examenes)-1:
        if i == examenes[K]:
            c_detectadas += 1
        K +=1

  return c_detectadas

N,K,examenes=leer_datos()
#print(copias_totales(examenes))
print(copias_detectadas(examenes,K))

"""
def main(nk: str, entrada: str=None):     n, k = nk.split()     n = int(n)     k = int(k)     if not entrada:         entrada = input()         memoria = []     repetidos_memoria = 0     repetidos_total = 0         for e in entrada.split():         if e in memoria[-k:]:             repetidos_memoria += 1         if e in memoria:             repetidos_total += 1         memoria.append(e)     return str(repetidos_memoria)+" "+str(repetidos_total) if __name__ == "__main__":     print(main(input()))


Este código me paso todas las pruebas en el primer intento
"""
