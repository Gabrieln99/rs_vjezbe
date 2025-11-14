# main.py - koristi paket shop
from shop import proizvodi, narudzbe

# 1) dodajemo proizvode u skladiste (4 proizvoda) -> ukupno 6 (2 početna + 4 dodana)
proizvodi_za_dodavanje = [
  {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
  {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
  {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
  {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(p)

print("Ukupno u skladistu:", len(proizvodi.skladiste), "elemenata (očekivano 6).")
for p in proizvodi.skladiste:
    p.ispis()

# 2) napravimo narudžbu: 2x Laptop, 1x Monitor, 3x Miš
naruceno = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1},
    {"naziv": "Miš", "cijena": 100, "narucena_kolicina": 3}
]

nar = narudzbe.napravi_narudzbu(naruceno)
if nar:
    nar.ispis_narudzbe()

# Ispis sažetka svih narudžbi
print("\nSažetak svih narudžbi (lista rječnika):")
print(narudzbe.Narudzba.sve_narudzbe)
