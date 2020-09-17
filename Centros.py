""" Aqui se van a recibir los valores de las listas y
se va a hacer un promedio el cual despues se va a guardar
estos promedios se van a convertir en los nuevos centros"""

import numpy as np

def centros(Datos):
    centros = []
    for l in Datos:
        centros.append(np.mean(l, axis=0))
    return centros
