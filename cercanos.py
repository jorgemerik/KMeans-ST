from distancia import distancia

def cercanos(puntos,centros):
    klistas = [[] for i in range(len(centros))]

    for pt in puntos:
        min = -1
        cidx = -1
        for idx,centro in enumerate(centros):
            val = distancia(pt,centro) #positive
            if min == -1 or val < min:
                min = val
                cidx = idx
        klistas[cidx].append(pt)

    return klistas
