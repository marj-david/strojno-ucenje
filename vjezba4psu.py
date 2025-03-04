#Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke. Program nakon toga treba tražiti linije
#oblika:
#X-DSPAM-Confidence: <neki_broj>
#koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti. Koristite
#datoteke mbox.txt i mbox-short.txt
#Primjer
#Ime datoteke: mbox.txt
#Average X-DSPAM-Confidence: 0.894128046745
#Ime datoteke: mbox-short.txt
#Average X-DSPAM-Confidence: 0.750718518519

ime_dat = input("Unesi ime datoteke: ")
i=0.0
sum=0.0

fhand = open(ime_dat)
for line in fhand:
    line = line.split()
    
    if "X-DSPAM-Confidence:" in line:
        i+=1
        sum += float(line[1])

print ("Average X-DSPAM-Confidence: ", sum/i)

fhand.close()