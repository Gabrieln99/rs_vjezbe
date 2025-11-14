
class Proizvod:
    def __init__(self, naziv: str, cijena: (int, float), dostupna_kolicina: int):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Proizvod: {self.naziv}, Cijena: {self.cijena} eur, Dostupna količina: {self.dostupna_kolicina}")


skladiste = [
    Proizvod("Telefon", 1500, 5),
    Proizvod("Tablet", 2500, 3)
]

def dodaj_proizvod(proizvod_dict):
 
    if not isinstance(proizvod_dict, dict):
        raise TypeError("Očekuje se rječnik sa specifikacijom proizvoda.")
    for k in ("naziv", "cijena", "dostupna_kolicina"):
        if k not in proizvod_dict:
            raise KeyError(f"Nedostaje ključ '{k}' u specifikaciji proizvoda.")
    p = Proizvod(proizvod_dict["naziv"], proizvod_dict["cijena"], proizvod_dict["dostupna_kolicina"])
    skladiste.append(p)
    return p
