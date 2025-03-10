#Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
#navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
#srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
#Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
#ispiše odgovarajuću poruku

list = []
cnt = 0


while True:
    print("Unesi broj, ako upises Done, program zavrsava: ")
    a=input()
    if a == "Done":
        break
    elif a!= str:
        list.append(int(a))
        cnt+=1

print (list)
print("Ukupan broj elemanata: ", cnt)
print ("Najmanji el: ", min(list))
print ("Najveci el: ", max(list))

srednja_v = sum(list)/cnt

print(srednja_v)

list.sort()
print("Sortirana list: \n", list)

