
"""


def provjera_lozinke(lozinka):

    if len(lozinka) < 8 or len(lozinka) > 15:
        return False, "Lozinka mora sadržavati između 8 i 15 znakova"
    
    ima_v_slovo = any(slovo.isupper() for slovo in lozinka)
    ima_broj = any(slovo.isdigit() for slovo in lozinka)

    if not (ima_v_slovo and ima_broj):
        return False, "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"
    
    zabranjene_lozinka = lozinka.lower()
    if "password" in zabranjene_lozinka or "lozinka" in zabranjene_lozinka:
        return False, "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"
    

    return True , "Lozinka je JAKA!"

while True:
    lozinka = input("Unesite lozinku: ")

    ispravna, poruka = provjera_lozinke(lozinka)
    print(poruka)

    if ispravna:
        break

print("Prijava uspješna!")



lozinka = input("Unesite lozinku: ")
provjera_lozinke(lozinka)

"""
"""

def filtriraj_parne_brojeve (lista):
    parni = []
    for x in lista:
        if x % 2 == 0:
            parni.append(x)

    return parni


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne_brojeve(lista)) # [2, 4, 6, 8, 10]


"""

"""
def uklanjanje_duplikata(lista):
    jedinstveni_brojevi = set()
    rezultat = []

    for x in lista:
        if x not in jedinstveni_brojevi:
            jedinstveni_brojevi.add(x)
            rezultat.append(x)

    return rezultat


lista = [1, 2, 2, 5,6,6, 3, 4, 5, 6, 7, 8, 9, 10,10]
print(uklanjanje_duplikata(lista)) # [2, 4, 6, 8, 10]
"""

"""

#RANDOM GENERIRANEJ HRVATSKOG BROJA MOBITELA


import random

def generiranje_broja():
    pozivni = random.choice(["091","092","095","097", "098", "099"])
    ostatak = "".join(str(random.randint(0,9)) for _ in range(7))
    return pozivni + ostatak



print (f"ovo je random generirani broj telefona:{generiranje_broja()}")

"""

"""
def filter_brojeva(lista):
    parni = []
    neparni =[]

    for x in lista:
        if x % 2 == 0:
            parni.append(x)
        else:
            neparni.append(x)
    return {"parni": parni, "neparni" : neparni}
    

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_brojeva(lista))

"""

