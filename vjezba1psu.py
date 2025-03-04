print("Unesi radne sate")
radni_sati = input()
radni_sati = int(radni_sati)
print ("\nUnesi satnicu")
satnica = input()
satnica = float(satnica)
zarada = radni_sati*satnica
print ("\nVasa ukupna zarada ovaj tjedan je: ", zarada)

def total_euro():
    zaradaf = radni_sati*satnica
    print("\nFunkcija je izracunala da ste zaradili: ", zaradaf)

total_euro()