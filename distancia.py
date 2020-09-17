#distancia.py
from scipy.spatial import distance

def distancia(a,b):
    dist = distance.euclidean(a, b)
    return dist
