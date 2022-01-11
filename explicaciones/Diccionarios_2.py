"""Script para explicar las funcionalidades de Diccionarios"""

# Estructura basica
d = dict({(2,"II")})
print(d)
print("elementos",len(d))

# CREAR DICCIONARIOS
# creamos un diccionario vacio o sin Pareja (clave: valor)
dic_persona = dict()
# OTRA FORMA DE CREAR un diccionario vacio o sin Pareja (clave: valor)
dic_empleados = {}
# asi creamos una tupla vacia
t1 = ()
# esto es igual, creamos una tupla vacia
t2 = tuple()
# así creamos una lista vacia
l1 = []
# esto es igual, creamos una lista vacia
l2 = list()


# CREAMOS UN DICCIONARIO DE CLAVES ENTERAS Y VALORES TEXTO
dic_estudiantes = {1012: "Maria", 2021: "Jose", 2902: "Juan", 764: "Pedro"}

# OTRA FORMA MAS COMODA DE CREAR  UN DICCIONARIO DE CLAVES TEXTO Y VALORES TEXTO
dic_asignaturas = {
    #codigo : Nombre
    "b12": "Calculo", 
    "a29": "Algoritmos",
    "z87": "Fisica",
    "d51": "Taller de programacion"
}

# CREAMOS UN DICCIONARIO QUE TIENE CLAVES TEXTO Y VALORES TIPO LISTA
dic_frabrica_autos = {
    # pais: [marca, marca, marca]
    "USA": ["Tesla","Buick","Lincoln","Dodge","Jeep","Cadillac","Chrysler","Ford","GMC","Chevrolet"]
    ,"Japon": ["Toyota", "Lexus", "Honda", "Mazda", "Nissan", "Datsun", "Nissan", "Suzuki", "Mitsubishi", "Isuzo", "Infiniti", "Subaru"]
    ,"Alemania": ["Audi", "BMW", "Mercedes Benz", "Volkswagen", "Porsche", "Opel", "Smart", "Alpina"]
    ,"Francia": ["Renault", "Peugeot", "Citroën", "Bugatti", "Alpine", "Venturi", "DS", "Aixam", "Ligier", "PGO"]
}

# CREAMOS UN DICCIONARIO QUE TIENE CLAVES TEXTO Y VALORES OTROS DICCIONARIOS CON CLAVE TEXTO Y VALOR TEXTO
dic_clientes = {
    #codigo : {"nombre":"valor", "email":"valor","telfono":"valor", "direccion":"valor"}
    "2829": {"nombre":"Pepito Perez", "email":"pepito.perez@gmail.com","telfono":"6789", "direccion":"Cartagena"},
    "678": {"nombre":"Pedro Villarreal", "email":"pedrito01@hotmail.com","telfono":"78902", "direccion":"Barranquilla"},
}

# OTRA FORMA DE CREAR DICCIONARIOS
dic_articulo = dict({"Arroz" : 2000, "Aceite" : 1500, "Yuca" : 1200, "Queso": 5000, "Suero": 1700, "Pan": 800, "Gaseosa" : 2200})
print(dic_persona)
print(dic_empleados)
print(t1)
print(t2)
print(l1)
print(l2)
print(dic_frabrica_autos)
print(dic_clientes)

# AGREGAR PAREJAS AL DICCIONARIO
# AGREGAMOS VARIAS PAREJAS (CLAVE = VALOR)
dic_persona = {}
dic_persona["cedula"] = 9080709
dic_persona["nombre"] = "Fulanito de Tal"
dic_persona["edad"] = 25
dic_persona["email"] = "fulanito@gmail.com"
dic_persona["telefono"] = "56784909"
dic_persona["genero"] = "Masculino"
dic_persona["direccion"] = "Cartagena"
dic_persona["peso"] = 81.8
dic_persona["altura"] = 1.82
print("Items:", len(dic_persona))
print("Contenido:",dic_persona)

# OBTENER EL VALOR DE UNA PAREJA CONOCIENDO LA CLAVE DEL DICCIONARIO
# SI LA CLAVE NO EXISTE EN EL DICCIONARIO, SE LANZARA UN ERROR
clave ="sueldo"
valor = dic_persona.get(clave)
if valor:
  print(clave,":",valor)
else:
  print(clave,"no existe")

# OBTENER UN CONJUNTO CON LAS CLAVES DE UN DICCIONARIO ESPECIFICO
# Set o conjunto. Secuencia no-ordenada de elementos.
claves = dic_persona.keys()
conjunto_claves = set (claves)
print(conjunto_claves)

# OBTENER EN UNA LISTA LOS VALORES DEL DICCIONARIO ESPECIFICADO
valores = dic_persona.values();
lista_valores = list(valores)
print(lista_valores)

#  RECORRAR UN DICCIONARIO CON FOR
for clave, valor in dic_persona.items():
  print(clave,": ", valor)

# USAR UN FOR PARA RECORRER LOS VALORES DEL DICCIONARIO
for valor in dic_persona.values():
  print(valor)

# USAR UN FOR PARA RECORRER Y MOSTRAR SOLO LAS CLAVES DEL DICCIONARIO
for clave in dic_persona.keys():
  print(clave)

# OTRA FORMA DE MOSTRAR EL CONTENIDO DE CADA PAREJA DEL DICCIONARIO
for clave in dic_persona.keys():
   print(clave,": ", dic_persona[clave])

# SABER CUANTAS CLAVES TIENE UN DICCIONARIO
total_parejas = len(dic_persona)
print("EL diccionario de personas tiene ", total_parejas, " parejas")

# ACTUALIZAR LA PAREJA CON CLAVE "cedula"
# SI LA CLAVE NO EXISTE EN EL DICCIONARIO, SE LANZARA UN ERROR
clave = "sueldo"
valor = 12000000
dic_persona[clave] = valor
print(clave,":", dic_persona[clave])
print(dic_persona)

# ACTUALIZAR LA PARAJA CON CLAVE "EDAD"
# SI LA CLAVE NO EXISTE EN EL DICCIONARIO, ENTONCE, 
# CREA UNA NUEVA PAREJA CON ES A CLAVE, NO LANZA UN ERROR
dic_persona.update({"edad": 29})

print("EDAD: ", dic_persona["edad"])

# Saber si un diccionario esta vacío
if dic_persona :
    print("Diccionario No esta vacío")
else:
  print("Diccionario no esta vacio")

# SABER SI EL DICCIONARIO TIENE UNA CLAVE
if "nombre" in dic_persona:
  print("NOMBRE: ", dic_persona["nombre"])
else:
  print("NOMBRE NO EXISTE")

# Saber si el Diccionario tiene X valor

if "cedula" in dic_persona :
  if dic_persona["cedula"] == 9080709 :
      print("La Cedula 9080709 si existe")
  else:
     print("La Cedula 9080709 NO existe")
else:
  print("Diccionario no tenie la Cedula")

# Otra forma de saber si un diccionario tiene o no un valor 
valores = dic_persona.values()
if "56784909" in valores : 
  print("El diccionario tiene el Telefono 56784909")
else:
  print("El diccionario NO tiene el Telefono 56784909")

# Copiar un diccionario en otro
dic_copia = dic_persona.copy()

# MOSTRAMOS EL CONTENIDO DE AMBOS DICCIONARIOS
print (dic_persona)
print("")
print("------------")
print(dic_copia)

# MODIFIQUEMOS EL CONTENIDO DEL DICCIONARIO COPIA 
# Y NOTEMOS QUE EL DICCIONARIO ORGINAL NO CAMBIA

# QUITEMOS LA PAREJA DEL EMAIL DEL DICCIONARIO COPIA
valor = dic_copia.pop("email")
print("Peso: ", valor, " eliminado del diccionario copia")

# MOSTRAMOS EL CONTENIDO DE AMBOS DICCIONARIOS
print("Diccionario ORIGINAL")
print("------------")
print (dic_persona)
print("")
print("Diccionario COPIA")
print("------------")
print(dic_copia)

# OTRA FORMA DE COPIAR UN DICCIONARIO EN OTRO 
# CREAR UN DICCIONARIO A PARTIR DE OTRO
dic_copia2 = dict (dic_persona)

# MOSTRAMOS EL CONTENIDO DE AMBOS DICCIONARIOS
print("Diccionario ORIGINAL")
print("------------")
print (dic_persona)
print("")
print("Diccionario COPIA")
print("------------")
print(dic_copia2)

# LIMPIAR EL DICCIONARIO
dic_copia.clear()

print( len(dic_copia), " valores en el Diccionario" )

#elimina el diccionario completo, no se puede utilizar mas
del dic_copia2


