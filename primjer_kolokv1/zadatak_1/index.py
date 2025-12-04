

from data.razredi_studenti import razredi_studenti

def dohvati_studente_iz_razreda(razredi_studenti: list, naziv_razreda: str) ->list:
    for razred in razredi_studenti:
        if razred["razred"] == naziv_razreda:
            return [s["ime_prezime"] for s in razred["studenti"]]
    return[]




def prosjek_studenta(razredi_studenti: list, ime_prezime: str) -> float :
    for r in razredi_studenti:
        for s in r["studenti"]:
            if s["ime_prezime"] == ime_prezime:
                brojac = int(0)
                suma = float(0)
                for o in s["kolegiji"]:
                    suma += o["ocjena"]
                    brojac+=1
                return suma/brojac
    return None


#  kvadrati = [x ** 2 for x in range(1, 11)]

broj_po_r = [{"naziv":r["razred"],"broj_s":len(r["studenti"])} for r in razredi_studenti]

surb = [{s["ime_prezime"]} for r in razredi_studenti if r["razred"] == "1B" for s in r["studenti"]]               

print("Svi studenti iz 1A:", dohvati_studente_iz_razreda(razredi_studenti, "1A"))

print(prosjek_studenta(razredi_studenti,"Ana Horvat"))

print(surb)