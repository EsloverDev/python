# def buenosdias():
#     print("buenos dias")

# buenosdias()

# buenosdias()

# buenosdias()
# print("continúe el código")

# def buenosdias2(nombre):
#     print("buenos dias, " + nombre)

# buenosdias2("Edwin")

# buenosdias2("Diana")

# buenosdias2("Nuby")

# def buenasnoches(nombre):
#     print("¡buenas noches!, ", nombre)
#     return "es hora de descansar"

# despedida = buenasnoches("reinaldo")
# print(despedida)
# print( buenasnoches("Juana"))

#def sumalista(lista = [1, 2, 3]):
#     """ Suma cada uno de los elementos existentes en la lista de entrada
#     parameters:
#     lista: numerical list
#     return:
#     suma: float
#     """
#      suma = 0
#     for elem in lista:
#         suma += elem
#     return suma
# mylist = [12.5, 10, 13.4, 13.22, 7, 2.34]
# suma1 = sumalista(mylist)
# print(suma1)

# suma2 =sumalista()
# print(suma2)

# print( sumalista())

# def sumalistas (lista1, lista2):
#     return sumalista(lista1) + sumalista(lista2)
# mylist1 = [1, 2, 3, 4]
# mylist2 = [1, 2, 3, 5]
# print( sumalistas(mylist1, mylist2))

"""funciones anónimas"""
# triple = lambda  x:x*3
# print(triple(2))

# suma = lambda x,y:x+y
# print(suma(12,1))

"""calcular los múltiplos de 3 en los elementos de una lista"""
# lista = [1, 5, 4, 6, 8, 11, 3, 12]
# newlist = list(filter(lambda x:(x%3==0), lista))
# print(newlist)

"""elevar los elementos de la lista al cuadrado"""
# lista = [1, 5, 4, 6, 8, 11, 3, 12]
# maplist = list(map(lambda x:x**2,lista))
# print(maplist)

"""crear una funcion y agregarle componentes"""
# class carro():
#     pass
# carro1 = carro()
# carro2 = carro()
# carro3 = carro()
# type(carro1)
# type(carro2)
# type(carro3)

# carro1.color = "Azul"
# carro1.marca = "Renault"
# print("el color del carro1 es: {}. y su marca es: {}".format(carro1.color, carro1.marca))

# class car():
#     color = ""
#     marca = ""
#     modelo = ""
#     encendido = False

#     def encender (self):
#         self.encendido = True
    
#     def apagar (self):
#         self.encendido = False

# car1 = car()
# car2 = car()
# car1.color = "Azul"
# car1.marca = "Renault"
# car1.modelo = "2005"
# car1.encender()
# print(car1.encendido)
# car1.apagar()
# print(car1.encendido)
# print("el color del car1 es: {}. su marca es: {}. y su modelo es: {}".format(car1.color, car1.marca, car1.modelo))