def ocisti_broj(broj):
    znakovi_za_izbaciti = [" ", "-", "(", ")", "\t", "\n"]
    for z in znakovi_za_izbaciti:
        broj = broj.replace(z, "")
    return broj


def normaliziraj(broj):
    if broj.startswith("+385"):
        broj = "0" + broj[4:]
    elif broj.startswith("00385"):
        broj = "0" + broj[5:]
    elif broj.startswith("385"):
        broj = "0" + broj[3:]
    return broj


def pronadi_pozivni(broj, tablica_brojeva):
    for entry in tablica_brojeva:
        pb = entry["pozivni_broj"]
        if isinstance(pb, list):
            for p in pb:
                if broj.startswith(p):
                    return p, entry
        else:
            if broj.startswith(pb):
                return pb, entry
    return None, None


def validiraj_broj_telefona(broj):
    rezultat = {
        "pozivni_broj": None,
        "broj_ostatak": None,
        "vrsta": None,
        "mjesto": None,
        "operater": None,
        "validan": False
    }

    # 1. Očisti
    broj = ocisti_broj(broj)

    # 2. Normaliziraj
    broj = normaliziraj(broj)

    # 3. Pronađi pozivni broj
    pozivni, entry = pronadi_pozivni(broj, tablica_brojeva)

    if not pozivni:
        return rezultat  # invalid, nepoznat pozivni

    rezultat["pozivni_broj"] = pozivni
    ostatak = broj[len(pozivni):]
    rezultat["broj_ostatak"] = ostatak

    # 4. Poznati tip broja
    vrsta = entry["vrsta"]
    rezultat["vrsta"] = vrsta

    # 5. Validacija ostatka
    if vrsta == "Posebne usluge":
        duljina_ok = len(ostatak) == 6
        rezultat["mjesto"] = None
        rezultat["operater"] = None
    elif vrsta == "Mobilna mreža":
        duljina_ok = len(ostatak) in (6,7)
        rezultat["mjesto"] = None
        rezultat["operater"] = entry["mjesto"]
    else:  # Fiksna mreža
        duljina_ok = len(ostatak) in (6,7)
        rezultat["mjesto"] = entry["mjesto"]
        rezultat["operater"] = None

    if duljina_ok:
        rezultat["validan"] = True

    return rezultat



print(validiraj_broj_telefona("091-722-33-11"))
print(validiraj_broj_telefona("+385 98 123 4567"))
print(validiraj_broj_telefona("00385972123456"))
print(validiraj_broj_telefona("021/456-789"))
