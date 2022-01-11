"""
    Script para explicar los conceptos básicos de POO
    Concepto: Los objetos son instancias de clases
"""

#1. Definir una clase
# Una clase es una plantilla para un objeto.

class Carro:
    pass

obj_carro = Carro()
print(obj_carro)
print(type(obj_carro))

# Podemos definir atributos dinámicos (NO ES UNA BUENA PRACTICA)
obj_carro.color = "Azul"
obj_carro.marca = "Ford"

print("El color de mi carro es {} y de marca {}".format(obj_carro.color,obj_carro.marca))

#2. Una clase con atributos de clase
class Carro2:
    color = ""
    marca = ""

obj_carro2 = Carro2()
print("Valores de atributos iniciales del objeto. Color: {}, Marca: {}".format(obj_carro2.color,obj_carro2.marca))
#Los puedo modificar.
obj_carro2.color = "Rojo"
obj_carro2.marca = "Nissan"

print("Valores de atributos del objeto ahora son. Color: {}, Marca: {}".format(obj_carro2.color,obj_carro2.marca))

#3. Métodos

class Carro3():
    color = ""
    marca = ""
    encendido = False

    def encender(self):
        self.encendido = True

    def apagado(self):
        self.encendido= False

obj3 = Carro3()
print(obj3.encendido)
obj3.encender()
print(obj3.encendido)