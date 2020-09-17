"""
Devuelve los puntos mas cercanos a los Centros (Puede ser mejorado,ej -> haciendo un sort y busqueda binaria)
"""

from distancia import distancia

def cercanos(puntos,centros):
    klistas = [[] for i in range(len(centros))]

    for pt in puntos:
        min = float('inf')
        cidx = -1
        for idx,centro in enumerate(centros):
            val = distancia(pt,centro) #positive
            if val < min:
                min = val
                cidx = idx
        klistas[cidx].append(pt)

    return klistas
