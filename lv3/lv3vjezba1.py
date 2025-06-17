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
data = pd.read_csv('mtcars.csv')

# 1. Kojih 5 automobila ima najveću potrošnju? (mpg - miles per gallon, manja vrijednost znači veću potrošnju)
top5_potrosnja = data.sort_values(by='mpg', ascending=True).head(5)
print("5 automobila s najvećom potrošnjom:")
print(top5_potrosnja[['car', 'mpg']])

# 2. Tri automobila s 8 cilindara s najmanjom potrošnjom
lowest_8cyl = data[data['cyl'] == 8].sort_values(by='mpg', ascending=False).head(3)
print("\nTri automobila s 8 cilindara s najmanjom potrošnjom:")
print(lowest_8cyl[['car', 'mpg']])

# 3. Srednja potrošnja automobila sa 6 cilindara
avg_mpg_6cyl = data[data['cyl'] == 6]['mpg'].mean()
print(f"\nSrednja potrošnja automobila sa 6 cilindara: {avg_mpg_6cyl:.2f} mpg")

# 4. Srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs
filtered_4cyl = data[(data['cyl'] == 4) & (data['wt'] * 1000 >= 2000) & (data['wt'] * 1000 <= 2200)]
avg_mpg_4cyl = filtered_4cyl['mpg'].mean()
print(f"\nSrednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs: {avg_mpg_4cyl:.2f} mpg")

# 5. Broj automobila s ručnim (am=1) i automatskim (am=0) mjenjačem
transmission_counts = data['am'].value_counts()
print(f"\nAutomatski: {transmission_counts[0]}, Ručni: {transmission_counts[1]}")

# 6. Automobili s automatskim mjenjačem i snagom preko 100 konjskih snaga
auto_over_100hp = data[(data['am'] == 0) & (data['hp'] > 100)]
print(f"\nBroj automobila s automatskim mjenjačem i snagom preko 100 KS: {len(auto_over_100hp)}")

# 7. Masa svakog automobila u lbs
print("\nMasa svakog automobila u lbs:")
print(data[['car', 'wt']])

