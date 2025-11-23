from podaci import tablica_brojeva

def ciscenje_broja(broj: str) -> str:
    znakovi = [" ", "/", "(", ")", "\n", "\t", "-", "_"]
    for z in znakovi:
        broj = broj.replace(z, "")
    return broj


def normalizacija_broja(broj: str) -> str:
    if broj.startswith("+385"):
        return "0" + broj[4:]
    if broj.startswith("00385"):
        return "0" + broj[5:]
    if broj.startswith("385"):
        return "0" + broj[3:]
    return broj


def pronadi_pozivni_broj(broj: str, tablica):
    for entry in tablica:
        pb = entry["pozivni_broj"]

        if isinstance(pb, list):
            for p in pb:
                if broj.startswith(p):
                    return p, entry
        else:
            if broj.startswith(pb):
                return pb, entry
    return None, None


def validiraj_duljinu(vrsta: str, ostatak: str) -> bool:
    if vrsta == "posebne usluge":
        return len(ostatak) == 6
    return len(ostatak) in (6, 7)

def validiraj_broj_telefona(broj:str):

    rezultat = {
        "pozivni_broj" : None,
        "broj_ostatak" : None,
        "vrsta": None,
        "mjesto": None,
        "operater": None,
        "validan": False
    }

    # 1. očisti
    broj = ciscenje_broja(broj)

    # 2. normaliziraj
    broj = normalizacija_broja(broj)

    # 3. pronađi pozivni
    pozivni, entry = pronadi_pozivni_broj(broj, tablica_brojeva)
    if not pozivni:
        return rezultat  # ne može pronaći pozivni broj

    rezultat["pozivni_broj"] = pozivni

    # 4. ostatak broja
    ostatak = broj[len(pozivni):]
    rezultat["broj_ostatak"] = ostatak

    # 5. vrsta broja
    vrsta = entry["vrsta"]
    rezultat["vrsta"] = vrsta

    # 6. validacija duljine
    if not validiraj_duljinu(vrsta, ostatak):
        return rezultat

    # 7. mapiranje
    rezultat["mjesto"] = entry.get("mjesto")
    rezultat["operater"] = entry.get("operater")

    # 8. označi kao valjan
    rezultat["validan"] = True

    return rezultat


# testovi
print(validiraj_broj_telefona("091 722 3311"))
print(validiraj_broj_telefona("+385 98 123 4567"))
print(validiraj_broj_telefona("00385(21)456789"))
print(validiraj_broj_telefona("0800 123456"))
