import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)

mpg = data[:,0]
hp = data[:,3]
wt = data[:,5]
cyl = data[:,1]

for n in wt:
    sizes = wt
    plt.plot(wt, sizes, marker=".", markeredgecolor='red') 

min_mpg = np.min(mpg)
max_mpg = np.max(mpg)
mean_mpg = np.mean(mpg)
print(f"Minimalna potrošnja: {min_mpg} mpg")
print(f"Maksimalna potrošnja: {max_mpg} mpg")
print(f"Srednja potrošnja: {mean_mpg:.2f} mpg")

mpg_6cyl = mpg[cyl == 6]
min_mpg_6 = np.min(mpg_6cyl)
max_mpg_6 = np.max(mpg_6cyl)
mean_mpg_6 = np.mean(mpg_6cyl)
print(f"(6 cilindara) Minimalna: {min_mpg_6} mpg, Maksimalna: {max_mpg_6} mpg, Srednja: {mean_mpg_6:.2f} mpg")

plt.scatter(mpg, hp)
plt.xlabel("MPG")
plt.ylabel("HP")
plt.title("Primjer")
plt.show()