"""
    Script para explicar composición y herencia.     
"""


#1. Objetos dentro de Objetos: Composición.
print("----------Punto 1---------------")
class Cancion:
    """
    Modela una canción
    Atributos:
        titulo (str): Titulo de la canción
        ano (int): ano de la canción
        compositor (str): Compositor
    """
    # Constructor de clase
    def __init__(self, titulo, ano, compositor):
        self.titulo = titulo
        self.ano = ano
        self.compositor = compositor
        print('Se ha creado la canción:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.compositor)


class Catalogo:
    """
    Modela un Catalogo de canciones
    Atributos:
        canciones (list): Lista de canciones inicial
    """

    def __init__(self, canciones=[]):
        self.canciones = canciones

    def agregar(self, p):  # p será un objeto Canción
        self.canciones.append(p)

    def mostrar(self):
        for p in self.canciones:
            print(p)  # Toma el método __str__ definido en la clase canción


c1 = Cancion("Bohemia Rhapsody", 1975, "Queen")
c2 = Cancion("Imagine", 1971, "Jhon Lennon")

c = Catalogo([c1,c2])  # Añado una lista con dos canciones desde el principio
c.mostrar()
c.agregar(Cancion("Start Me up", 1981, "The Rolling Stones"))  # Añadimos otra cancion
c.mostrar()


#Composición en UML. Generación de diagramas con el Lenguaje Unificado de Modelado (UML).
#Permiten forjar un lenguaje visual común en el complejo mundo del desarrollo de software 


# 2. La herencia es la capacidad que tiene una clase de heredar los atributos y métodos de otra,
# algo que nos permite reutilizar código y hacer programar mucho más óptimos.
print("----------Punto 2---------------")

class Producto:
    """
    Describe un producto de una tienda
    """
    def __init__(self,codigo,nombre,precio_venta,descripcion):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.descripcion = descripcion

    def __str__(self):
        return 'COD: {}, {}, Precio: {}'.format(self.codigo,self.nombre,self.precio_venta)



class Alimento(Producto):
    """
    Describe un alimento de una tienda
    """

    def __init__(self,codigo,nombre,precio_venta,descripcion,productor,fecha_vencimiento):
        Producto.__init__(self,codigo,nombre,precio_venta,descripcion)
        self.productor = productor
        self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        return Producto.__str__(self) + ", Productor: {} , Fecha Vencimiento: {}".format(self.productor,self.fecha_vencimiento)

class Libro(Producto):
    """
    Describe un libro  de una tienda
    """


    def __init__(self,codigo,nombre,precio_venta,descripcion,isbn,autor):
        Producto.__init__(self,codigo,nombre,precio_venta,descripcion)
        self.isbn = isbn
        self.autor = autor

    def __str__(self):
        return Producto.__str__(self) + ", ISBN: {} , Autor: {}".format(self.isbn,self.autor)


#Notese la sobrecarga = polimorfismo
libro1 = Libro("LCF1234","La mil y una noches",12345.65,"Este libro trata de...","AS1234","Edward William Lane")
libro2 = Libro("ME456","Cien años de soledad",2345.65,"Esta obra maestra...","BX345","Gabriel García Marquez")

print(libro1)
print(libro2)

producto1 = Producto("LM345","Lampara bacarrat 100 años",12345668,"Esta lampara es una..")
print(producto1)

alimento1= Alimento("SPI34","Sopas instantaneas rasputin",1200,None,"Pastas la muñeca","2019/12/24")
print(alimento1)

# 3. Nos permite evitar el llamado explicito a los metodos de la superclase
print("----------Punto 3---------------")

class Libro2(Producto):
    """
    Describe un libro  de una tienda
    """


    def __init__(self,codigo,nombre,precio_venta,descripcion,isbn,autor):
        super().__init__(codigo,nombre,precio_venta,descripcion)
        self.isbn = isbn
        self.autor = autor

    def __str__(self):
        return super().__str__() + ", ISBN: {} , Autor: {}".format(self.isbn,self.autor)
print("Libro de la clase Libro2 utilizando super()")
libro_clase_nueva = Libro2("LCF1234","La mil y una noches",12345.65,"Este libro trata de...","AS1234","Edward William Lane")

print(libro_clase_nueva)

# 4. Herencia múltiple
print("----------Punto 4---------------")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

cube = Cube(2)
print("Surface area : {}".format( cube.surface_area()))
print("Volume: {}".format(cube.volume()))