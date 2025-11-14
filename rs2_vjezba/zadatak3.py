"""

# 1. Koristeći list comprehension, izgradite listu parnih kvadrata brojeva od 20 do 50

parni_kvadrati = [x**2 for x in range(20, 51) if x % 2 == 0]
print(parni_kvadrati)

"""


"""
# 2  Koristeći list comprehension, izgradite listu duljina svih nizova u listi sadrže slovo a: 

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk",
          "čokolada", "ples", "pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(r) for r in rijeci if "a" in r]
print(duljine_sa_slovom_a)

"""
"""
#3. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi brojevi od 1 do 10, a vrijednosti su 
# kubovi tih brojeva, ali samo za neparne brojeve, za parne brojeve neka vrijednost bude sam broj:

kubovi = [{i: (i**3 if i % 2 != 0 else i)} for i in range(1, 11)]
print(kubovi)

"""

"""

# 4. Koristeći dictionary comprehension, izgradite rječnik iteriranjem kroz listu brojeva od 50 do 500 s 
 # korakom 50, gdje su ključevi brojevi, a vrijednosti su korijeni tih brojeva zaokruženi na 2 decimale:


import math
korijeni = {i: round(math.sqrt(i), 2) for i in range(50, 501, 50)}
print(korijeni)

"""

"""
# 5. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi prezimena studenata, a vrijednosti 
# su zbrojeni bodovi, iz liste studenti :

studenti = [
 {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
 {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
 {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
 {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
 {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
 {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni_bodovi = [{s["prezime"]: sum(s["bodovi"])} for s in studenti]
print(zbrojeni_bodovi)

"""

"""

# 6. Koristeći dictionary comprehension, izgradite rječnik gdje su ključevi brojevi od 1 do 10, a vrijednosti su 
# liste faktorijela tih brojeva.


import math
faktorijeli = {i: [math.factorial(k) for k in range(1, i+1)] for i in range(1, 11)}
print(faktorijeli)

"""



