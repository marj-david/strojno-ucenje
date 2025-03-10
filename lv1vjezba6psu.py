#Napišite Python skriptu koja će učitati tekstualnu datoteku naziva SMSSpamCollection.txt [1]. Ova datoteka 
#sadrži 425 SMS poruka pri čemu su neke označene kao spam, a neke kao ham.

fopen = open("SMSSpamCollection.txt", "r", encoding="utf-8")
spamcnt = 0
hamcnt = 0

spamwords = 0
hamwords = 0
exclamation = 0

for line in fopen:
    line = line.strip()
    if line.startswith("spam"):
        spamcnt += 1
        words = line.split(" ")
        for words in line:
            spamwords += 1
        if line.endswith("!"):
            exclamation += 1
            
    elif line.startswith("ham"):    
        hamcnt += 1
        words = line.split(" ")
        for words in line:
            hamwords += 1

print("Prosjecan broj rijeci u Spam porukama: ", spamwords/spamcnt)
print("Prosjecan broj rijeci u Ham porukama: ", hamwords/hamcnt)
print ("Broj spam poruka koje završavaju sa usklicnikom: ", exclamation)