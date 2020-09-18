# KMeans-ST

Por: *Stephan Guingor*, *Jorge Merikanskas*, *Emilio Arce*, *Rodrigo Murillo*



#### Creamos una implementacion de el algoritmo de clasificacion *KMeans*

```python
# Ejemplo Basico
from kmeans import KMeansTec
from sklearn.datasets.samples_generator import make_blobs

# Some Data
X, y_true = make_blobs(n_samples=300, centers=4,
                         cluster_std=0.60, random_state=0)

kmeans = KMeansTec(n_clusters=4)
kmeans.fit(X)
y_predict = kmeans.predict(X)

# To Get centers
kmeans.centers

```

Despues se puede graficar

```python
plt.scatter(X[:, 0], X[:, 1], s=50, c=y_kmeans,cmap='coolwarm');
plt.scatter([c[0] for c in km.centers ], [c[1] for c in km.centers ], c='black', s=200, alpha=0.5);
```

![Clustering Plot]()
