"""

#zad1

from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina: {self.godina_proizvodnje}, Kilometraža: {self.kilometraza} km")

    def starost(self):
        return datetime.now().year - self.godina_proizvodnje

auto = Automobil("Honda", "Civic", 2012, 175000)
auto.ispis()
print("Starost automobila:", auto.starost(), "godina")

"""

"""
#zad2   

import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return None

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        def safe_sqrt(x):
            return math.sqrt(x) if x >= 0 else None
        return safe_sqrt(self.a), safe_sqrt(self.b)

k = Kalkulator(9, 3)
print(k.zbroj(), k.oduzimanje(), k.mnozenje(), k.dijeljenje(), k.potenciranje(), k.korijen())

"""

"""

#zad3

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene) if self.ocjene else 0

    def __repr__(self):
        return f"{self.ime} {self.prezime} ({self.prosjek():.2f})"

studenti = [
 {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5,4,3,5,2]},
 {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3,4,5,2,3]},
 {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5,5,5,5,5]},
 {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2,3,2,4,3]},
 {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4,4,4,3,5]},
 {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5,5,5,5,5]}
]

studenti_objekti = [Student(s['ime'], s['prezime'], s['godine'], s['ocjene']) for s in studenti]


najbolji_student = max(studenti_objekti, key=lambda st: st.prosjek())

for st in studenti_objekti:
    print(st.prezime, "-", f"{st.prosjek():.2f}")
print("Najbolji student:", najbolji_student.prezime, najbolji_student.prosjek())
"""
"""
#4 zadatak

import math

class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * self.r * self.r

k = Krug(3.5)
print(f"Opseg: {k.opseg():.2f}, Površina: {k.povrsina():.2f}")


"""

# 5 zadatak

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}.")

    def __repr__(self):
        return f"Radnik({self.ime}, {self.pozicija}, placa={self.placa})"

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, worker: Radnik, povecanje):
        worker.placa += povecanje
        print(f"{worker.ime} je dobio povišicu od {povecanje}. Nova plaća: {worker.placa}")

# primjer
radnik = Radnik("Luka", "inženjer", 8000)
manager = Manager("Ana", "manager", 12000, "IT")

radnik.work()               
manager.work()             
print("Prije:", radnik)
manager.give_raise(radnik, 1000)
print("Poslije:", radnik)

