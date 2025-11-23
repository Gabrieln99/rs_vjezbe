#Objasniti kako se event loop izvrsava : PITANJE ZA KOLOKVIJI

"""
import asyncio

async def korutina():
    return "123"

async def main():
    rezultat_1 = await korutina()
    rezultat_2 = await korutina()
    rezultat_3 = await korutina()


    #event loop 
    asyncio.run(main)
    
    """

"""

# async def autentifikacija():


async def timer(sec : int):
    print(f"Izvršavam timer {sec}")
    await asyncio.sleep(sec)
    print(f"Završavam cekanje timer {sec}")
    return f"Rezultat timera {sec}"

async def main():
    #stvaranje korutine objekata : timer(n)

    #task_1 = asyncio.create_task(timer_cor_1)
    #task_2 = asyncio.create_task(timer_cor_2)          # to nam ne treba kada koristimo gather
    #task_3 = asyncio.create_task(timer_cor_3)

    lista_korutina = [timer(n) for n in range(1,6)]

    rezultat = await asyncio.gather(*lista_korutina)

    rezultat= await asyncio.gather(timer_cor_1)     #schedule and run andd44
    print(rezultat)

    
    #event loop 
    asyncio.run(main())


"""



# OVDJE PRIJE SVEGA TREBA INSTALIRATI ENVIREMENET OD CONDE  
"""
import requests
import aiohttp


response = requests.get("http://www.catfact.ninja/fact")  # HTTP GET zahtjev

response_dict = response.json()


lista = []

t1 = time.perf_counter()

for i in range (30):
    print(f"Šaljem request za fact {i}")
    response = requests.get("http://www.catfact.ninja/fact")
    lista.append(response.json()["fact"])
t2 = time.perf_counter()



aiohttp.ClientSession()
print(lista)
print(f"Vrijeme izvrsavanja {round(t2 - t1, 2)}")
"""
"""
import asyncio
import requests
import aiohttp
import time

# context manager se koristi za I/O operacije
# with


#asyncroni context manager


async def dohvati_cat_fact():
        async with aiohttp.ClientSession() as session:
            response = await session.get("http://www.catfact.ninja/fact")


async def main():

    
        print(response)
    print("zavrsava main korutina")


aiohttp.ClientSession()
print(lista)
print(f"Vrijeme izvrsavanja {round(t2 - t1, 2)}")

"""

import asyncio
import aiohttp
import time

async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    async with session.get(url) as response:
        return await response.json()
    
async def main():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session) for _ in range(5)]
        rezultat = await asyncio.gather(*tasks)
        print(rezultat)


asyncio.run(main())


#ovdje sada treba raspakirati, treba izvuci imena korsinika, emailove korsinika, username korisnika




#print("Imena korisisnika", names)
#print("Emailovi korisisnika", emails)
#print("USernamovi korisisnika", usernames)




