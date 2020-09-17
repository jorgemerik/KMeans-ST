""" Aqui se van a recibir los valores de las listas y
se va a hacer un promedio el cual despues se va a guardar
estos promedios se van a convertir en los nuevos centros"""

import numpy as np

def centros (Datos):

    centro = np.mean(Datos, axis=0)

    return centro
