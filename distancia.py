"""
Devuelve la distancia euclideana entre dos klistas
"""
#distancia.py
from scipy.spatial import distance
# np.sqrt(np.sum((np.array(b)-np.array(a))**2))
def distancia(a,b):
    dist = distance.euclidean(a, b)
    return dist
