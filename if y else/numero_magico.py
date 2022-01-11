numero_magico=12345679
numero_usuario=int(input("digite un número entr 1 y 9: "))
if(numero_usuario<1 or numero_usuario>9):
    print("debes ingresar un numero entero entre 1 y 9")
else:
    numero_magico*=numero_usuario*9
    print(numero_magico)
