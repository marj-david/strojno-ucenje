#Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao 
#ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka 
#riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.

song = open("song.txt", "r")
rijecnik = {}
for line in song:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in rijecnik:
            rijecnik[word] += 1
        else:
            rijecnik[word] = 1

print (rijecnik)

for word in rijecnik:
    if rijecnik[word] == 1:
        print(word)

song.close()
