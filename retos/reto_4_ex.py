
#list(map(int,input().split()))
def leer_datos():
    n, k = input().split()
    examenes = list(map(int,input().split()))
    return int(n), int(k), examenes

# def copias_totales(examenes):
#     c_totales = 0
#     if examenes.count(examenes[0])==len(examenes):
#         c_totales = (examenes)-1
#     else:
#         valores = set(examenes)
#         print(valores)
#         for i in valores:
#             if i in examenes:
#                 c_totales += examenes.count(i)-1

def copias_totales(examenes):
    c_totales = 0
    c_totales = len(examenes) - len(set(examenes))
    
    return c_totales

def copias_detectadas(examenes,k):
    c_detectadas = 0
    copias = 0
    for i in examenes:
        if k <= len(examenes)-1:
            if i == examenes[k]:
                c_detectadas += 1
                k +=1
        
    return c_detectadas

 
n, k, examenes = leer_datos()
print(copias_totales(examenes))

"""
def main(nk: str, entrada: str=None):
    n, k = nk.split()
    n = int(n)
    k = int(k)
    if not entrada:
        entrada = input()
    
    memoria = []
    repetidos_memoria = 0
    repetidos_total = 0
    
    for e in entrada.split():
        if e in memoria[-k:]:
            repetidos_memoria += 1
        if e in memoria:
            repetidos_total += 1
        memoria.append(e)


    return str(repetidos_memoria)+" "+str(repetidos_total)



if __name__ == "__main__":
    print(main(input()))
"""
