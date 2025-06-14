# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 12:08:00 2018

@author: Grbic
"""

from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.io import imread, imsave
from sklearn.cluster import KMeans


# Učitavanje i obrada slike
# Učitavanje slike u nijansama sive
face = mpimg.imread('example_grayscale.png')
if len(face.shape) == 3:
    face = np.mean(face, axis=2)
    
X = face.reshape((-1, 1)) 
k_means = cluster.KMeans(n_clusters=5, n_init=10)
k_means.fit(X) 
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = face.shape

plt.figure(1)
plt.imshow(face,  cmap='gray')
plt.show()

plt.figure(2)
plt.imshow(face_compressed,  cmap='gray')
plt.show()

#kvantizacija slike koristeći KMeans
image = imread("example.png")
original_shape = image.shape

pixels = image.reshape(-1, 3)

kmeans = KMeans(n_clusters=12, random_state=42)
kmeans.fit(pixels)
quantized_pixels = kmeans.cluster_centers_[kmeans.labels_]

quantized_image = quantized_pixels.reshape(original_shape).astype(np.uint8)

imsave("quantized_example.png", quantized_image)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Quantized Image')
plt.imshow(quantized_image)
plt.axis('off')

plt.show()