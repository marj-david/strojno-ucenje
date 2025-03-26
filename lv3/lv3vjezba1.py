#Za mtcars skup podataka napišite programski kod koji će odgovoriti na sljedeća pitanja:
#1. Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
#2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
#3. Kolika je srednja potrošnja automobila sa 6 cilindara?
#4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
#5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
#6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
#7. Kolika je masa svakog automobila u kilogramima?


import pandas as pd
import numpy as np
mtcars = pd.read_csv('mtcars.csv')

print(mtcars.sort_values(by='mpg', ascending=False)[0:5])
print(mtcars[mtcars.cyl==8], mtcars.sort_values(by="mpg", ascending = True)[0:3])

new_cars = mtcars[mtcars.cyl==6]
new_cars = new_cars.groupby('mpg')
print(new_cars['mpg'].mean())

new_cars4 = mtcars[(mtcars.cyl==4) & ((mtcars.wt > 2.000) & (mtcars.wt <2.200))]
print(new_cars4['mpg'].mean())

rucni = 0
autom = 0

print("Rucni: ", rucni)
print("Automatik: ", autom)


