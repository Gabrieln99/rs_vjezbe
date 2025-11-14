#zadatci skripte Rs1

""" 
a = 5
a = "Hello, World!" # može i s jednostrukim navodnicima
print(a) # Hello, World!



print("Hello world")

"""
"""

a = 5 
b = 10 

print(a + b)  # Zbrajanje
print(a - b)  # Oduzimanje  
print(a * b)  # Množenje
print(a / b)  # Dijeljenje
print(a // b) # Cjelobrojno dijeljenje
print(a % b)  # Modulo
print(a ** b) # Stepenovanje

"""


""" 
a = 5
a = "Hello, World!" # može i s jednostrukim navodnicima
print(a) # Hello, World!



print("Hello world")

"""
"""

a = 5 
b = 10 

print(a + b)  # Zbrajanje
print(a - b)  # Oduzimanje  
print(a * b)  # Množenje
print(a / b)  # Dijeljenje
print(a // b) # Cjelobrojno dijeljenje
print(a % b)  # Modulo
print(a ** b) # Stepenovanje

"""




"""
#Zadatak 1


broj_1 = float(input("unesite prvi broj"))


broj_2 = float(input("unesite drugi broj"))


operator = input("unesite operator")

dozvoljeni_operatori = ["+", "-", "*", "/"]

if operator not in dozvoljeni_operatori:
    print("Nepodržani operator!")

if operator == "+":
    rezultat = broj_1 + broj_2
    print(f"Rezultat operacije {broj_1}  + {broj_2} je {rezultat}")

elif operator == "-":
    print(f"Rezultat operacije {broj_1}  - {broj_2} je {broj_1 - broj_2}")

elif operator == "*":
    print(f"Rezultat operacije {broj_1}  * {broj_2} je {broj_1 * broj_2}")

elif operator == "/":

    if broj_2 == 0:
        print("Dijeljenje s nulom nije dozvoljeno")

    print(f"Rezultat operacije {broj_1}  / {broj_2} je {broj_1 / broj_2}")


"""


"""
#Zadatak 1



print("unesite prvi broj")
a = float(input())

print("unesite drugi broj")
b = float(input())

print("unesite operator")
operator = input()

match operator:
    case "+":
        rezultat = a + b
        print("rezultat operacije", a, operator, b, "je", rezultat)
    case "-":
        rezultat = a - b
        print("rezultat operacije", a, operator, b, "je", rezultat)
    case "*":
        rezultat = a * b
        print("rezultat operacije", a, operator, b, "je", rezultat)
    case "/":
        if b == 0:
            print("Dijeljenje s nulom nije dozvoljeno!")
        else:
            rezultat = a / b
            print("rezultat operacije", a, operator, b, "je", rezultat)
    case _:
        print("Nepodržani operator")


"""

"""
#Zadatak 2


godina = int(input("unesite godinu: "))

if(godina %4 == 0 and godina %100 != 0) or(godina %400 == 0):
    print(f"Godina {godina}. je prijestupna ")

else:
    print(f"Godina {godina}. nije prijestupna ") 


"""
"""
#ZADATAK 2

print("program za provjeravanje prjestupne godine")

print("unesite godinu:")
a = int(input())

if (a % 4 == 0 and a % 100 != 0 ) or (a % 400 == 0):
    print("godina ",  a , " je pristupna" )
else : 
    print("godina", a , "nije prijestupna ")


"""

"""

import random

print("pogodite broj o d 1 do 100: ")

print("unesite jedan broj: ")

a = int(input())

broj = random.randint(1,100)

while a != broj:
    print("ponovno unesite broj vas broj nije tocan")

    if (a < broj):
        print("unjeli ste previse mali broj ")
    elif (a > broj):
        print("Unjeli set pre veliki broj ")

    a = int(input())

print("pogodili ste broj")



"""

"""
#zadatak 2

print("program za provjeravanje prjestupne godine")

print("unesite godinu:")
a = int(input())

if (a % 4 == 0 and a % 100 != 0 ) or (a % 400 == 0):
    print("godina ",  a , " je pristupna" )
else : 
    print("godina", a , "nije prijestupna ")


"""


"""
#ZADATAK 3

tajni_broj = 50

broj_je_pogoden = False
brojac = 0; 

while not broj_je_pogoden:
    broj = int(input("Pogodi broj: "))
    brojac += 1

    if broj < tajni_broj:
        print("pokusaj ponovno broj premalen")
    elif broj > tajni_broj:
        print("pokusaj ponovno broj prevelik")
    else:
        print(f"Broj je pogoden: {broj}")
        print(f"bravo pogodio si broj u {brojac} pokušaja.")
        broj_je_pogoden = True
        
print("igra je gotova")

"""

"""

#ZADATAK 3 

import random

print("pogodite broj o d 1 do 100: ")

print("unesite jedan broj: ")

a = int(input())

broj = random.randint(1,100)

while a != broj:
    print("ponovno unesite broj vas broj nije tocan")

    if (a < broj):
        print("unjeli ste previse mali broj ")
    elif (a > broj):
        print("Unjeli set pre veliki broj ")

    a = int(input())

print("pogodili ste broj")



"""
"""
#zadatak 4


brojevi = []


while True:
    broj = int(input(f"Unesite neki broj, ako zelite zaustaviti program kliknite 0!"))

    if broj == 0:
        print("Unjeli ste 0, kraj programa!")
        break
    else:
        brojevi.append(broj)
        print(f"Broj koji ste unijeli je {broj}, i  spremljen je .Unesite sljedeci broj")

zbroj = sum(brojevi)
print(f"zbroj svih brojeva koje ste unijeli je: {zbroj}. " )


"""

"""
#LISTE

sastojci = ["sol", "ulje", "papar", "tortilje", "meso"]

sastojci.append("Vegeta")
sastojci.insert(2, "Paprika")

sastojci.remove("ulje")

print(sastojci)




#Rjecnik

klijent = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}


for kljuc, vrijendonst in klijent.items():
    print(kljuc, vrijendonst)

"""


"""
#  Vježba 5

for i in range(1, 2): #zato sto petlja for se korsiti za ponavljanje iteraacija vise puta , ovdje ce se izvrsiti samo 1
 print(i)


for i in range(10, 1, 2):
 print(i) # nista jer program ne moze krenut sa veceg broaj na manji i da se dize svaka 2 broja , 0 nije manje od 1, pa se petlja ne pokreće ni jednom.
 

for i in range(10, 1, -1):
 print(i) # e ova petlja ce raditi jer krece sa 10 i zadali smo mu da ide prema dole do 1 ali bez nje znaci do dvojke 
"""
"""
# Vježba 6:
# Napišite program koji ispisuje sumu svih parnih brojeva od 1 do 100 (uključivo).
 
suma = 0
for i in range (1,101):
    if i % 2 == 0:
        suma += i
print(f"suma svih parnih brojeva je : {suma}")



"""
"""

#Napišite program koji ispisuje prvih 10 neparnih brojeva u obrnutom redoslijedu


neparni_brojevi = []

for i in range(1, 20, 2):  
    neparni_brojevi.append(i)


for broj in reversed(neparni_brojevi):
    print(broj)
"""

"""
#zadatak 7

def provjera_lozinka(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("lozinka mora sadrzavati izmedu 8 i 15 znakova")
        return
    ima_veliko = any(slovo.upper() for slovo in lozinka)
    ima_broj = any(slovo.isdigit() for slovo in lozinka)

    if not (ima_veliko and ima_broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return
    

    mala_lozinka = lozinka.lower()
    if "password" in mala_lozinka or "lozinka" in mala_lozinka:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return
    
    print("Lozinka je jaka")

if __name__ == "__main__":
    lozinka = input("Unesite lozinku: ")
    provjera_lozinka(lozinka)
    
    
"""
"""
#zadatak 8
def filtriraj_parne(lista):
    parni = []  
    for x in lista:
        if x % 2 == 0:
            parni.append(x)
    return parni  

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista))

"""
"""

#zadatak 9


def ukloni_duplikate(lista):
    jedinstveni_brojevi = set()
    rezultat = []

    for x in lista:
        if x not in jedinstveni_brojevi:
            jedinstveni_brojevi.add(x)
            rezultat.append(x)
    
    return rezultat

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))

"""
"""
#zadatak 10 

def brojanje_riječi (tekst):

    tekst = tekst.lower()

    rijeci = tekst.split()
    broj_ponavljanja = {}

    for r in rijeci:
        if r in broj_ponavljanja:
            broj_ponavljanja[r] = broj_ponavljanja[r] + 1
        else:
            broj_ponavljanja[r] = 1

    return broj_ponavljanja


tekst = "Python, python je programski jezik koji je jednostavan za učenje i učenje i korištenje. Python je vrlo popularan."
print(brojanje_riječi(tekst))
    
"""
"""

# Zadatak 11

def grupiraj_po_paritetu(lista):
    parni = []
    neparni = []

    for broj in lista:
        if broj % 2 == 0:
            parni.append(broj)
        else:
            neparni.append(broj)

    return {"parni": parni, "neparni": neparni}



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))

"""

"""
# Zadatak 12

def obrni_rjecnik(rjecnik):
    novi_rjecnik = {}

    for kljuc, vrijednost in rjecnik.items():
        novi_rjecnik[vrijednost] = kljuc

    return novi_rjecnik

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(f"primarni rjecnik: {rjecnik}")
print("obrnuti redsoljed")
print(obrni_rjecnik(rjecnik))


#ili
# Zadatak 12

def obrni_rjecnik(rjecnik):
    kljucevi = []   # lista za ključeve
    vrijednosti = []  # lista za vrijednosti

    # prolazimo kroz originalni rječnik
    for kljuc in rjecnik:
        kljucevi.append(kljuc)
        vrijednosti.append(rjecnik[kljuc])

    # stvaramo novi rječnik tako da zamijenimo uloge
    novi_rjecnik = {}

    for i in range(len(kljucevi)):
        novi_rjecnik[vrijednosti[i]] = kljucevi[i]

    return novi_rjecnik


# Test primjer
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))


"""
"""
#zadatak13
#tocka1

def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista))

#tocka2

def maks_i_min(lista):
    maks = lista[0]
    min = lista[0]

    for broj in lista:
        if broj > maks:
            maks = broj
        if broj < min:
            min = broj

    return(maks, min)


lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista))



#tocka3




def presjek (skup_1,skup_2):
    return (skup_1.intersection(skup_2))


skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))

"""

"""

# s+zadatak 14


def isPrime(broj):
    if broj <= 1:
        return False
    for i in range(2, broj):
        if broj % i == 0:
            return False
    return True


def primes_in_range(start, end):
    prosti = []
    for broj in range(start, end + 1):
        if isPrime(broj):
            prosti.append(broj)
    return prosti

print(primes_in_range(1, 10))   
print(primes_in_range(10, 30))  
 
"""
# Zadatak 15


def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    broj_samoglasnika = 0
    broj_suglasnika = 0

    for znak in tekst:
        if znak in vowels:
            broj_samoglasnika += 1
        elif znak in consonants:
            broj_suglasnika += 1

    return {"vowels": broj_samoglasnika, "consonants": broj_suglasnika}


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))


