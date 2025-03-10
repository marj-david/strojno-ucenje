#Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i
#1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). Također, ako je
#broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.

try:
    print("Unesi ocjenu izmedju 0.0 i 1.0: ")
    a = input()
    a = float(a)

    if a < 0.0 or a > 1.0:
        print("Greska")

    elif a>= 0.9:
        print("Ocjena je A")

    elif a>= 0.8:
        print ("Ocjena je B")

    elif a>=0.7:
        print ("Ocjena je C")

    elif a>=0.6:
        print ("Ocjena je D")

    elif a<0.5:
        print ("Ocjena je F")

except:
    print("An exception occurred")
