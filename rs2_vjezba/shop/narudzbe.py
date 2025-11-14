
from .proizvodi import skladiste, Proizvod

class Narudzba:

    sve_narudzbe = []

    def __init__(self, skladiste_snapshot, naruceni_proizvodi, ukupna_cijena):
        self.skladiste = skladiste_snapshot
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        items = ", ".join([f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi])
        print(f"Naručeni proizvodi: {items}, Ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(naruceni_proizvodi):

    if not isinstance(naruceni_proizvodi, list):
        print("Argument naruceni_proizvodi mora biti lista.")
        return None
    if len(naruceni_proizvodi) == 0:
        print("Lista narucenih proizvoda ne smije biti prazna.")
        return None

    for el in naruceni_proizvodi:
        if not isinstance(el, dict):
            print("Svaki element u listi mora biti rječnik.")
            return None
        for k in ("naziv", "cijena", "narucena_kolicina"):
            if k not in el:
                print(f"Svaki rječnik mora sadržavati ključ '{k}'.")
                return None

    skladiste_map = {p.naziv: p for p in skladiste}
    for stavka in naruceni_proizvodi:
        naziv = stavka["naziv"]
        trazena = stavka["narucena_kolicina"]
        if naziv not in skladiste_map:
            print(f"Proizvod {naziv} nije dostupan!")
            return None
        if skladiste_map[naziv].dostupna_kolicina < trazena:
            print(f"Proizvod {naziv} nije dostupan!")
            return None

    ukupna_cijena = sum(item["cijena"] * item["narucena_kolicina"] for item in naruceni_proizvodi)


    for stavka in naruceni_proizvodi:
        naziv = stavka["naziv"]
        trazena = stavka["narucena_kolicina"]
        skladiste_map[naziv].dostupna_kolicina -= trazena

  
    nar = Narudzba(skladiste, naruceni_proizvodi, ukupna_cijena)
    Narudzba.sve_narudzbe.append({
        "proizvodi": naruceni_proizvodi,
        "ukupna_cijena": ukupna_cijena
    })
    return nar
