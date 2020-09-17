"""
calcula los centroides que mejor quedan con los Datos
"""

import numpy as np
import random

from cercanos import cercanos
from Centros import centros
from distancia import distancia



def kmeans(puntos,k,it=100):
    cent = random.sample(list(puntos),k)
    for i in range(it):
        clusters = cercanos(puntos,cent)
        cent  = centros(clusters)

    return cent


class KMeansTec:
    def __init__(self,n_clusters):
        self.k = n_clusters
        self.points = None
        self.centers = None

    def fit(self,X,**kw):
        self.points = X
        self.centers = kmeans(self.points,self.k,**kw)

    def predict(self,X):
        """
        Returns Array With Class prediction (Could be improved using nearest 'logic')
        """
        if not self.centers:
            raise ValueError("Call Fit First!")
        prediction = []
        for point in X:
            min = float('inf')
            cidx = 0
            for idx,center in enumerate(self.centers):
                val = distancia(point,center) #positive
                if val < min:
                    min = val
                    cidx = idx
            prediction.append(cidx)
        return prediction




# N =100

# x = np.random.rand(N)
# y = np.random.rand(N)

# data = [[x,y] for x,y in zip(x,y) ]
