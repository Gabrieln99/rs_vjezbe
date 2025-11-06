from podatci import tablica_brojeva
import re


def validiraj_broj_telefona(broj_telefona: str) -> dict:
    if not isinstance(broj_telefona, str):
        raise ValueError("Broj telefona mora biti string.")

    broj_telefona = re.sub(r'\D+', '', broj_telefona)

 
    if broj_telefona.startswith('00385'):
        broj_telefona = broj_telefona[5:]
    elif broj_telefona.startswith('385'):
        broj_telefona = broj_telefona[3:]

    if len(broj_telefona) < 5:
        return {
            "pozivni_broj": None,
            "broj_ostatak": broj_telefona,
            "vrsta": None,
            "mjesto": None,
            "operater": None,
            "validan": False
        }

 
    return usporedba_s_bazom(broj_telefona, tablica_brojeva)


def usporedba_s_bazom(broj_telefona: str, baza: list) -> dict:
   
    if not broj_telefona.startswith('0'):
        broj_telefona = '0' + broj_telefona

  
    if broj_telefona.startswith('0800'):
        pozivni_broj = '0800'
        validne_duljine = {6}
    elif broj_telefona.startswith('01'):
        pozivni_broj = '01'
        validne_duljine = {6, 7}
    else:
        pozivni_broj = broj_telefona[:3]
        validne_duljine = {6, 7}

    broj_ostatak = broj_telefona[len(pozivni_broj):]

   
    zapis_brojevi = next(
        (
            d for d in baza
            if pozivni_broj in (
                d['pozivni_broj']
                if isinstance(d['pozivni_broj'], list)
                else [d['pozivni_broj']]
            )
        ),
        None
    )

    return {
        "pozivni_broj": pozivni_broj,
        "broj_ostatak": broj_ostatak,
        "vrsta": zapis_brojevi["vrsta"] if zapis_brojevi else None,
        "mjesto": zapis_brojevi["mjesto"] if zapis_brojevi else None,
        "operater": zapis_brojevi.get("operater") if zapis_brojevi and "operater" in zapis_brojevi else None,
        "validan": len(broj_ostatak) in validne_duljine
    }



print(validiraj_broj_telefona("+385919306351"))

