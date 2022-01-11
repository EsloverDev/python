while True:
    n, m = [int(x) for x in input().split()]
    if n > 0:
        break

terrenos = []
for i in range(m):
    while True:
        fila = input().split()
        if fila[2].isnumeric() and int(fila[2]) >= 0:
            break
    terrenos.append([int(fila[0]), int(fila[1]), int(fila[2]), fila[3]])

antenas = {'a': 2600, 'b': 19000, 'c': 1500, 'd':19600, 'e':6500}

departamentos = {i: {j:0 for j in antenas} for i in range(1,n+1)}
for fila in terrenos:
    dep, area, cant, tipo = fila[:]
    if dep in departamentos and tipo in antenas:
        area_restante = area - cant * 11700
        cant_nuevas = area_restante / antenas[tipo]
        if cant_nuevas < 0:
            cant_nuevas = 0
        departamentos[dep][tipo] = round(cant_nuevas)

for clave in departamentos:
    total_ant = sum([departamentos[clave][ant] for ant in antenas])
    ant_max, cant_max = max(departamentos[clave].items(), key=lambda x: x[1])
    ant_min, cant_min = min(departamentos[clave].items(), key=lambda x: x[1])
    print(clave)
    print(total_ant)
    print(ant_min, cant_min)
    print(ant_max, cant_max)

for ant in antenas:
    dep_min, cant_ant_min = min(departamentos.items(), key=lambda x: x[1][ant])
    dep_max, cant_ant_max = max(departamentos.items(), key=lambda x: x[1][ant])
    cant_ant_max, cant_ant_min = cant_ant_max[ant], cant_ant_min[ant]
    print(dep_min, ant, cant_ant_min)
    print(dep_max, ant, cant_ant_max)
