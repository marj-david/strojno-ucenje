import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mtcars = pd.read_csv('mtcars.csv')

# 1. Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara.

cet = mtcars[mtcars.cyl == 4]
cet=cet["mpg"].to_numpy().mean()
sest = mtcars[mtcars.cyl == 6]
sest=sest["mpg"].to_numpy().mean()
osm = mtcars[mtcars.cyl == 8]
osm=osm["mpg"].to_numpy().mean()

sve = np.array([cet,sest,osm])
print(sve)
bla = ["4", "6","8"]
print(bla)

plt.bar(bla,sve)
plt.ylabel("MPG")
plt.xlabel("PISTONS")
plt.title("potrošnju automobila s 4, 6 i 8 cilindara")
plt.show()



#2. Pomoću boxplot-a prikažite na istoj slici distribuciju težine automobila s 4, 6 i 8 cilindara.

cetwt = mtcars[mtcars.cyl == 4]
cetwt=cetwt["wt"].to_numpy()

sestwt = mtcars[mtcars.cyl == 6]
sestwt=sestwt["wt"].to_numpy()

osmwt = mtcars[mtcars.cyl == 8]
osmwt=osmwt["wt"].to_numpy()

#autiwt=np.array([cetwt*1000,sestwt*1000,osmwt*1000])

fig = plt.figure(figsize =(10, 7))

# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])

# Creating plot
bp = ax.boxplot(autiwt)

# show plot
plt.show()
