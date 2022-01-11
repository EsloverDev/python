"""
    Script para explicar lo que es un constructor
    Constructor: En programación orientada a objetos (POO), un constructor es una subrutina cuya misión es 
    inicializar los atributos de un objeto de una clase.
    Constructor en Python: El método __init__ es el encargado de fungir como constructor
    es decir que este va a inicializar una serie de atributos y ejecutar el código que le definamos
    al momento de que se cree un objeto de la clase, al ser llamado "__init__".
"""

# Clase Gato con constructor
print("----------Punto 1---------------")
class Gato:
    """
    Clase Gato ejemplo constructor
    """
    familia = 'felino' # atributos de clase, compartidos por todas las instancias
    
    def __init__(self, nombre):
        self.nombre = nombre # atributos de instancia únicos para cada instancia

x = Gato('Tino')
y = Gato('Osiris')
print(x.familia) # compartido por todos los objetos de la clase gato
print(y.familia) # compartido por todos los objeto de la clase gato

print(x.nombre) # único para x
print(y.nombre) # único para y

#Que pasa si no especifico el atributo del constructor.
#z = Gato()

# 2. Cuidado con los atributos de clase 
print("----------Punto 2---------------")
class Gato2:
    """
    Clase Gato 2 ejemplo constructor con error en los atributos de clase
    """
    familia = 'felino' # atributos de clase compartida por todas las instancias
    
    mis_duenos = [] #Dueños del gato. Este es un uso incorrecto de atributos de clase.

    def __init__(self, nombre):
        self.nombre = nombre # atributos instancia únicos para cada instancia

    def agregar_duenos(self, nombre_dueno):
        self.mis_duenos.append(nombre_dueno)

a = Gato2('Magna')
b = Gato2('Merchan')
a.agregar_duenos('Fernando Perez')
b.agregar_duenos('Juana Rodriguez')
print(a.mis_duenos) # comparten los mismos dueños


# 3. Correción del diseño anterior
print("----------Punto 3---------------")
class Gato3:
    """
    Clase Gato 3 correción de diseño
    """
    familia = 'felino' # atributos de clase compartida por todas las instancias
    

    def __init__(self, nombre):
        self.nombre = nombre # atributos clase únicos para la instancia
        self.mis_duenos = [] #Crea una lista de dueños para cada gato.


    def agregar_duenos(self, nombre_dueno):
        self.mis_duenos.append(nombre_dueno)

c = Gato3('Magna')
d = Gato3('Merchan')
c.agregar_duenos('Fernando Perez')
d.agregar_duenos('Juana Rodriguez')
print("Dueños del gato c: ",c.mis_duenos) # Ahora son solo del objeto c 
print("Dueños del gato d: ",d.mis_duenos) # Ahora son solo del objeto d 

# 4. Otros métodos especiales
print("----------Punto 4---------------")

class GatoDestructor:
    """
    Clase Gato Destructor Método __del__
    """
    def __del__(self):
        print("El objeto se está borrando de la memoria")

r = GatoDestructor()
del(r)
# r.__del__() #Equivalente

class Gato4:
    """
    Clase Gato 4 Método __str___
    """
    familia = 'felino' # atributos de clase compartida por todas las instancias

    def __init__(self, nombre):
        self.nombre = nombre # atributos clase únicos para la instancia
        self.mis_duenos = [] #Crea una lista de dueños para cada gato.


    def agregar_duenos(self, nombre_dueno):
        self.mis_duenos.append(nombre_dueno)

    def __str__(self):
       return f"Soy un gato de nombre {self.nombre} y mis dueños son {self.mis_duenos}."

h = Gato4("Goliat")
h.agregar_duenos("Samuel Noreña")
h.agregar_duenos("Bibiana Ruiz")
print(h)