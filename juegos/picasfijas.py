"""
--> 1345 <- digitos son unicos 
i:  1893 -> 1 fija (1) , 1 pica (3)
i:  3674 -> 2 picas (3,4)
i:  1543 -> 2 fija, 2 picas
i:  1345 -> 4 fijas, Fin del juego

"""
import random

def comparar (numero_secreto,numero):
    contador_picas=0
    contador_fijas=0
    indice=0
    while indice<4:
        if numero[indice] == numero_secreto[indice]: 
            contador_fijas+=1
        elif numero[indice] in numero_secreto:
            contador_picas+=1   
        indice+=1       
    
    return contador_picas,contador_fijas

def generar_numero_secreto():
    lista_numeros=["0","1","2","3","4","5","6","7","8","9"]
    secreto = ""
    while len(secreto)<4:
        numero = random.choice(lista_numeros)
        if numero not in secreto:
            secreto+=numero
    
    return secreto


def iniciar_juego():
    numero_secreto =  generar_numero_secreto()  
  #  print("Numero Secreto ->",numero_secreto)
    fijas=0
    while fijas!=4:
        numero = input("numero : ")
        picas,fijas = comparar(numero_secreto,numero)
        print(f"Tiene {picas} picas y {fijas} fijas")
    print("Fin del Juego ! ...")

def run(): 
    select = "1"
    while select != "0":
        iniciar_juego()
        select = input(" 0 - Para salir, cualquier otra tecla para jugar de nuevo <- ")

if __name__=="__main__":
    run()