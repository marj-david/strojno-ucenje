#Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. Koristite ugrađenu
#Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. Na kraju prepravite
#rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.
#Primjer:
#Radni sati: 35 h
#eura/h: 8.5
#Ukupno: 297.5 eura

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
