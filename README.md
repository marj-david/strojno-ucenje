# strojno-ucenje
Kodovi sa labosa

LV4

1. Pokrenite primjer 4.1. iz dodatka. U ovom primjeru generiraju se umjetni podaci te se izgrađuje linearni regresijski model.
Razmislite koji dio programskog koda odgovara kojem dijelu teorije predstavljene u opisu ove vježbe.

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y
def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy
x = np.linspace(1,10,100)
y_true = non_func(x)
y_measured = add_noise(y_true)

    -Stvaranje ulaznih i izlaznih podataka za model

plt.figure(1)
plt.plot(x, y_measured, 'ok', label='mjereno')
plt.plot(x, y_true, label='stvarno')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)

  - Postavlja ulazne izlazne podatke na graf (funkcija)

indeksi_train = indeksi[0:int(np.floor(0.7*len(x)))]
indeksi_test = indeksi[int(np.floor(0.7*len(x)))+1:len(x)]

xtrain = x[indeksi_train]
ytrain = y_measured[indeksi_train]
xtest = x[indeksi_test]
ytest = y_measured[indeksi_test]

  - dijeljenje podataka na test i train

linearModel = lm.LinearRegression()
linearModel.fit(xtrain, ytrain)

   - Treniranje linearnog modela

MSE_test = mean_squared_error(ytest, ytest_p)

  - MSE test

2. Pokrenite primjer 4.2. iz dodatka. U ovom primjeru generiraju se umjetni podaci te se izgrađuje linearni regresijski model.
Međutim, ovaj model se proširuje polinomskim članovima prema (4-11). Koja je razlika u odnosnu na rezultate dobivene
u zadatku 1?

U drugom primeju koristimo polinomske članove. U prvom primjeru će regresijska linija biti ravna crta, što neće nužno pratiti točan izgled funkcije, za razliku od drugog primjera gdje će rezultantna regresijska krivulja biti kompleksna polinomijalna funkcija, što će dati točniji rezultat

4.
   1. Koliko mjerenja (automobila) je dostupno u datasetu?
      Dostupno je 6699 mjerenja
   2. Kakav je tip pojedinog stupca u dataframeu?
    name           6699 non-null   object
    year           6699 non-null   int64
    selling_price  6699 non-null   float64
    km_driven      6699 non-null   int64
    fuel           6699 non-null   object
    seller_type    6699 non-null   object
    transmission   6699 non-null   object
    owner          6699 non-null   object
    mileage        6699 non-null   float64        
    engine         6699 non-null   int64
    max_power      6699 non-null   float64        
    seats          6699 non-null   int64

  3. Koji automobil ima najveću cijenu, a koji najmanju?
   name  year  selling_price  km_driven    fuel seller_type transmission        owner  mileage  engine  max_power  seats
4778  Maruti 800 AC  1997      10.308919      80000  Petrol  Individual       Manual  Third Owner     16.1     796       37.0      4
                       name  year  selling_price  km_driven    fuel seller_type transmission        owner  mileage  engine  max_power  seats
2591  BMW X7 xDrive 30d DPE  2020      15.789592       5000  Diesel  Individual    Automatic  First Owner    13.38    2993      265.0      7
     
  4. Koliko automobila je proizvedeno 2012. godine?
     575
  5. Koji automobil je prešao najviše kilometara, a koji najmanje?
     Benzinci srednja vrijedost km: 54101.882809861534
Dizelasi srednja vrijednost km: 88039.97234392114
  8. Koliko najčešće automobili imaju sjedala?
  9. Kolika je prosječna prijeđena kilometraža za automobile s dizel motorom, a koliko za automobile s benzinskim
     motorom?

LV5

1. a) Pokrenite skriptu i pogledajte dobiveni dijagram raspršenja. Što primjećujete?
   Primjećujemo da što je temperatura i razina CO2 u sobi veća, to znači da je veća vjerojatnost da je ona zauzeta.
   b) Koliko podatkovnih primjera sadrži učitani skup podataka?
   Podatkovni skup sadrži 10129 primjera
   c) Kakva je razdioba podatkovnih primjera po klasama?
   Binarni klasifikacijski problem

2. e) Što se događa s rezultatima ako se koristi veći odnosno manji broj susjeda?
   Povećavanjem broja susjeda smanjujemo razlike između podataka, odnosno riješavamo se šuma. Smanjivanjem dobivamo oštrije razlike
   f) Što se događa s rezultatima ako ne koristite skaliranje ulaznih veličina?
   Rezultati se ne mijenjaju bitno
