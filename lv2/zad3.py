import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("tiger.png")
img = img[:,:,0].copy()

#povećava svjetlinu svakog piksela za 100
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i, j] = min(img[i, j] + 100, 255)

#rotira sliku za 90 stupnjeva u smjeru kazaljke na satu
img = np.rot90(img, -1)

#zrcali sliku
img = np.fliplr(img)

#smanji rezoluciju slike 10 puta
img = img[::10, ::10]

#prikaži četvrtinu slike po širini prikazati sliku cijelu po visini; ostali dijelovi slike trebaju biti 
#crni

img = img[:, :img.shape[1] // 4]
# Postavljanje crnih dijelova slike
img = np.pad(img, ((0, 0), (0, img.shape[1] // 3)), mode='constant', constant_values=0)
# Prikaz slike


plt.figure()
plt.imshow(img, cmap="gray")
plt.show()
