import os
os.system('CLS')


def agrerar(datos):
    global error
    lista = []
    lista.insert(0, int(datos[0]))
    lista.insert(1, datos[1])
    lista.insert(2, float(datos[2]))
    lista.insert(3, int(datos[3]))
    if lista[0] in db.keys() or lista[1] in db.values():
        error = True
        return error
    else:
        llave = lista[0]
        lista.pop(0)
        db[llave] = lista
        return db


def borrar(datos):
    global error
    lista = {}
    lista[0] = int(datos[0])
    lista[2] = float(datos[2])
    lista[3] = int(datos[3])
    llave = lista[0]
    if llave in db.keys():
        lista.pop(0)
        if lista in db.values():
            db.pop(llave)
            return db
        else:
            error = True
    else:
        error = True
        return error


def actualizar(datos):
    global error
    lista = {}
    lista[0] = int(datos[0])
    lista[2] = float(datos[2])
    lista[3] = int(datos[3])
    llave = lista[0]
    if llave in db.keys():
        lista.pop(0)
        for i in range(3):
            db[llave][i] = lista[i]
        return db
    else:
        error = True
        return error


def crear_db():
    db = {
        1: ["Manzanas", 6000.0, 25],
        2: ["Limones", 2500.0, 15],
        3: ["Peras", 2700.0, 33],
        4: ["Arandanos", 9300.0, 34],
        5: ["Tomates", 2100.0, 42],
        6: ["Fresas", 4100.0, 10],
        7: ["Helado", 4500.0, 41],
        8: ["Galleta", 500.0, 8],
        9: ["Chocolate", 4500.0, 80],
        10: ["Jamon", 15000.0, 10]
    }
    return db


def comparar(limite, tipo):
    contador = 0
    for x in db.values():
        if tipo == 0:
            if limite < x[1]:
                limite = x[1]
                llave = contador
                contador += 1
            else:
                contador += 1
        else:
            if limite > x[1]:
                limite = x[1]
                llave = contador
                contador += 1
            else:
                contador += 1
    lista_llaves = list(db.keys())
    nombre = db[lista_llaves[llave]][0]
    return nombre


if __name__ == '__main__':
    # ingresar la accion a realizar
    global error
    error = False
    db = crear_db()
    accion = input()
    if accion == "AGREGAR":
        # solicitud de los datos
        datos_ingreso = input().split()

        agrerar(datos_ingreso)
    elif accion == "BORRAR":
        datos_ingreso = input().split()

        borrar(datos_ingreso)
    elif accion == "ACTUALIZAR":
        datos_ingreso = input().split()

        actualizar(datos_ingreso)
    if error:
        print("ERROR")

    else:
        nombre_mayor = comparar(0, 0)
        nombre_menor = comparar(1000000, 1)
        suma = 0
        inventario = 0
        for x in db.values():
            suma += x[1]
        promedio = suma/len(db)
        for p in db.values():
            inventario += (p[1]*p[2])

    print(nombre_mayor, nombre_menor, round(promedio, 1), round(inventario, 1))
