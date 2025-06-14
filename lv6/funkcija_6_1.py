from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage


def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

#Stvaranje podataka i klasteriranje
n_samples = 500
flagc = 5
X= generate_data(n_samples, flagc)

kmeans = KMeans(n_clusters=3, random_state=42)  
kmeans.fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_


plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Cluster Centers')
plt.title('KMeans Clustering')
plt.xlabel('Znacajka 1')
plt.ylabel('Znacajka 2')
plt.legend()
plt.show()

# Određivanje optimalnog broja klastera
inertia_values = []
silhouette_scores = []
cluster_range = range(2, 21)  
for k in cluster_range:
	kmeans = KMeans(n_clusters=k, random_state=0)
	kmeans.fit(X)
	inertia_values.append(kmeans.inertia_)
	

plt.figure(figsize=(10, 7))
plt.plot(cluster_range, inertia_values, marker='x')
plt.title('Vrijednost kriterijske funkcije za različit broj klastera')
plt.xlabel('Broj klastera')
plt.ylabel('Kriterijska vrijednost')
plt.grid()
plt.show()

X = generate_data(25, 5)
Z = linkage(X, method="ward")

plt.figure(figsize=(10, 7))
dendrogram(Z, labels=[f"Podatak {i+1}" for i in range(len(X))])
plt.ylabel('Udaljenost')
plt.show()