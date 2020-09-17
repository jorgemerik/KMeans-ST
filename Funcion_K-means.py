import numpy as np
import random
import matplotlib.pyplot as plt
from cercanos import cercanos
from Centros import centros
from sklearn.datasets.samples_generator import make_blobs



def kmeans(puntos,k,it=100):
    cent = random.sample(list(puntos),k)
    for i in range(it):
        clusters = cercanos(puntos,cent)

        cent  = centros(clusters)

    return cent


# N =100

# x = np.random.rand(N)
# y = np.random.rand(N)

# data = [[x,y] for x,y in zip(x,y) ]

if __name__ == "__main__":
    X, y_true = make_blobs(n_samples=300, centers=4,
                           cluster_std=0.60, random_state=0)
    plt.scatter(X[:, 0], X[:, 1], s=50);

    # KMeans Via Us
    cent = kmeans(X,k=4)

    plt.scatter([c[0] for c in cent ], [c[1] for c in cent ], c='black', s=200, alpha=0.5);
    plt.show()

    # Sklearn KMeans
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)

    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);


    print(f"Sklearn -> {centers} | US -> {cent}")

    plt.show()
