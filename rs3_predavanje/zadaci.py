
import asyncio
import random
import time

# 1. Definirajte korutinu koja će simulirati dohvaćanje podataka s weba
# 

"""

async def dohvati_podatke():
    data = [i for i in range(1, 11)]
    await asyncio.sleep(3)  
    print("Podaci dohvaćeni.")
    return data

async def main():
    result = await dohvati_podatke()
    print("Rezultat:", result)

"""



# zad 2. Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba.
"""

async def dohvati_korisnika():
    await asyncio.sleep(3)
    korisnici = [
        {"id": 1, "ime": "Ana"},
        {"id": 2, "ime": "Marko"}
    ]
    return korisnici

async def dohvati_proizvod():
    await asyncio.sleep(5)
    proizvodi = [
        {"id": "A1", "ime": "Laptop"},
        {"id": "B2", "ime": "Tipkovnica"}
    ]
    return proizvodi

async def main():
    korisnici, proizvodi = await asyncio.gather(dohvati_korisnika(), dohvati_proizvod())
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)


"""

# 3  Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na poslužiteljskoj strani.

"""

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik_iz_baze: dict, lozinka: str):

    await asyncio.sleep(2)
    korisnicko_ime = korisnik_iz_baze['korisnicko_ime']
    
    for entry in baza_lozinka:
        if entry['korisnicko_ime'] == korisnicko_ime:
            if entry['lozinka'] == lozinka:
                return f"Korisnik {korisnicko_ime}: Autorizacija uspjelea."
            else:
                return f"Korisnik {korisnicko_ime}: Autorizacija neusp."
    return f"koorisnik {korisnicko_ime}: Lozinnka niej pronadena u bazi."

async def autentifikacija(korisnik: dict, lozinka: str):

    await asyncio.sleep(3)
   
    for entry in baza_korisnika:
        if (entry['korisnicko_ime'] == korisnik.get('korisnicko_ime') and
            entry['email'] == korisnik.get('email')):
         
            return await autorizacija(entry, lozinka)
  
    return f"Korisnik {korisnik} nije pronaden ."


async def main():
    korisnik_test = {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'}
    lozinka_test = 'super_teska_lozinka' 
    rezultat = await autentifikacija(korisnik_test, lozinka_test)
    print(rezultat)



"""
#4. Definirajte korutinu provjeri_parnost koja će simulirati "super zahtjevnu operaciju" provjere parnost
"""

async def provjeri_parnost(broj: int):
    await asyncio.sleep(2)  
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."

async def main():

    brojevi = [random.randint(1, 100) for _ in range(10)]
    print("Brojevi:", brojevi)

    zadaci = [asyncio.create_task(provjeri_parnost(b)) for b in brojevi]

    rezultati = await asyncio.gather(*zadaci)
    for r in rezultati:
        print(r)

"""
# 5. Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka.

"""

async def secure_data(osjetljivi: dict):
    await asyncio.sleep(3)  

    broj_kartice_enc = str(hash(osjetljivi['broj_kartice']))
    cvv_enc = str(hash(osjetljivi['CVV']))
    return {
        'prezime': osjetljivi['prezime'],
        'broj_kartice': broj_kartice_enc,
        'CVV': cvv_enc
    }

async def main():
    lista = [
        {'prezime': 'Horvat', 'broj_kartice': '4111111111111111', 'CVV': '123'},
        {'prezime': 'Nevak', 'broj_kartice': '5555555555554444', 'CVV': '456'},
        {'prezime': 'Kovacč', 'broj_kartice': '378282246310005', 'CVV': '789'}
    ]

    zadaci = [asyncio.create_task(secure_data(d)) for d in lista]
    rezultati = await asyncio.gather(*zadaci)
    for r in rezultati:
        print(r)

"""


# 6Kako možete unutar main korutine natjerati event loop da obuhvati ispis unutar korutine 


"""

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"

async def main():
    # stavljamo na scheudole obje korutine 
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))  # NE awaitamo task2 

    # awaitamo samo task1
    result1 = await task1
    print("Fetch 1 uspješno završen.")

    # Da bi se task2 imao vremena dovršiti i ispisati svoj tekst,
    # moramo držati event loop aktivnim dovoljno dugo — npr. kratkim sleep-om
    # duljim od parametra (2s). Time dokazujemo da ispis iz fetch_data(2)
    # može nastati bez da ga direktno awaitamo

    await asyncio.sleep(2.1)

    return [result1]

if __name__ == "__main__":
    t1 = time.perf_counter()
    results = asyncio.run(main())
    t2 = time.perf_counter()
    print(results)
    print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")

"""




# 7. Objasnite korak po korak kako se ponaša event loop



async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers)

asyncio.run(main())



"""  

1. Stvaranje zadataka

Kad napišeš create_task(timer(...)), Python samo zabilježi da taj zadatak postoji.
Ne počinje odmah — samo stoji u redu i čeka start.

2. Prvo pokretanje

Event loop krene pokretati svaki zadatak sve dok ne naiđe na prvo await.
U timeru to je odmah nakon što ispiše prvi redak.

3. Čekanje

Kad dođe do await asyncio.sleep(1), zadatak zaspi na 1 sekundu.
Dok spava, ne troši CPU — samo čeka.

4. Buđenje

Nakon 1 sekunde event loop probudi zadatak i kaže mu: “Nastavi gdje si stao!”.
Zadatak opet radi sve dok ne dođe do sljedećeg await.

5. Ponovljeni ciklus
Svaki timer radi:...



6. Stanja kroz koja prolazi task

Scheduled kreiran, ali još nije pokrenut

Running. trenutno se izvršava

Waiting. čeka zbog await sleep

Done. završio


Za kraj gateher samo nam govori doslovno Ne zavrsavaj main dok Svi tajmeri ne zavrse 

event loop u meduvremenu aktivira svaki tajmer svaku 1 sec . 

to nam je to 


"""



if __name__ == "__main__":
    asyncio.run(main())

