class Student:
    def __init__(self, ime: str, prezime: str, razred: str, kolegij_ocjene: dict):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.kolegij_ocjene = kolegij_ocjene


    def prosjek_ocjena(self) -> float:
        if not self.kolegij_ocjene:
            return 0.0
        
        prosjek = sum(self.kolegij_ocjene.valus()) / len(self.kolegij_ocjene)

        return round(prosjek, 1)
    


    def promjena_razreda(self, novi_razred: str) -> None:
    # Uvezi podatke
    from fakultet.podaci import razredi_studenti
    
    # Napravi listu svih dopuštenih razreda
    dopusteni_razredi = [razred["razred"] for razred in razredi_studenti]
    # Rezultat: ["1A", "1B"]
    
    # Provjeri je li novi razred dopušten
    if novi_razred not in dopusteni_razredi:
        raise ValueError(f"Razred {novi_razred} nije dopušten.")
    
    # Ako je OK, promijeni razred
    self.razred = novi_razred
