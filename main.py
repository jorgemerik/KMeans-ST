import numpy as np
import random
import matplotlib.pyplot as plt
from cercanos import cercanos
from Centros import centros
from sklearn.datasets.samples_generator import make_blobs
from kmeans import *
from pprint import pprint

if __name__ == "__main__":
    X, y_true = make_blobs(n_samples=300, centers=4,
                           cluster_std=0.60, random_state=0)



    # KMeans Via Us
    # cent = kmeans(X,k=4)
    k = 4
    km = KMeansTec(n_clusters=k)
    km.fit(X)
    y_kmeans = km.predict(X)
    # print(y_kmeans)
    plt.subplot(121)
    plt.grid(True)
    plt.title("Nuestro")
    plt.scatter(X[:, 0], X[:, 1], s=50, c=y_kmeans,cmap='coolwarm');
    plt.scatter([c[0] for c in km.centers ], [c[1] for c in km.centers ], c='black', s=200, alpha=0.5)


    # Sklearn KMeans
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    # print(y_kmeans)
    plt.subplot(122)
    plt.title("Sklearn")
    plt.grid(True)
    # Plot Clusters
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

    pprint(f"Sklearn -> {centers} |\n US -> {km.centers}")

    plt.show()


    # We could add metrics to check the data
