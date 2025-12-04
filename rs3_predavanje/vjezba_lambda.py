

"""
def kvadriraj(x):
    return x**2

print("Unesite broj koji želite kvadrirati:")
x = int(input())

print(f"Nakon kvadriranja rezultat je {kvadriraj(x)}")
"""


#lambda x: x**2
#print((lambda x: x**2)(5))


#kvadriraj = lambda x: x**2
#print(kvadriraj(4))


zbroj = lambda x,y: x + y
print (zbroj(3,4))

kvad_zbroj = lambda x,y: x**2 + y**2
print(kvad_zbroj(5,5))


moje_ime = lambda ime="Gabriel": f"Moje ime je: {ime}"
print(moje_ime())


godine = lambda br_godina=20, ime="Gabriel": f"Zovem se {ime} i imam {br_godina}"
print(godine())



mnozac = lambda x, factor = 2 : x * factor 
print(mnozac(10))



def primjeni_na_sve(lista, funkcija):
    rezultat = []
    for x in lista:
        rezultat.append(funkcija(x))
    return rezultat


uvecaj_za_tot = lambda broj: broj +5

print(primjeni_na_sve([1,2,3,4,5], uvecaj_za_tot))

# print(primjeni_na_sve([1,2,3,4,5], lambda x:x**3))







lista = [1,2,3,4,5]

kvadriraj = lambda x:x**2

kvadirana_lista = list(map(kvadriraj,lista))

#ili

kvadirana_lista = list(map(lambda x:x**2,lista))




# jmbagovi = list(map(lambda student:student["jmbag"], studneti))



kvadrati = [x**2 for x in range(1,11)]
print(kvadrati)



nizovi = ["jabuka", "kruška", "banana", "naranča"]

duljine = [len(niz) for niz in nizovi]
print(duljine)


studenti = [
  {"ime": "Ivan", "prezime": "Ivić", "godina_rodenja": 2000},
  {"ime": "Marko", "prezime": "Marković", "godina_rodenja": 1990},
  {"ime": "Ana", "prezime": "Anić", "godina_rodenja": 2003},
  {"ime": "Petra", "prezime": "Petrić", "godina_rodenja": 2001}
]

rodeni_prije_1999 = [student["ime"] for student in studenti if student["godina_rodenja"]]
print(rodeni_prije_1999)




