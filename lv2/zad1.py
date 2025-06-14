import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 3, 1])
y = np.array([1, 2, 2, 1, 1])


plt.plot(x, y, marker='*', markersize=7, markerfacecolor='red', markeredgecolor='red', linestyle='-', linewidth=2, color='blue')

plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Primjer")

plt.xlim(0, 4)
plt.ylim(0, 4)
plt.grid(True)
plt.show()

