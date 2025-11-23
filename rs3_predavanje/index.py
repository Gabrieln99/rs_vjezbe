"""
import asyncio
import time

async def funkcija():
    print("nesto")
    print(asyncio.get_event_loop())
    await asyncio.sleep(2) # I/O non blocking funkcija
    print("nesto drugo")
    return "Nesto trece"

asyncio.run(funkcija()) 
print(asyncio.get_event_loop())


"""
"""
async def korutina(param:int):
    print(f"Korutina je pokrenuta sa parametrom: {param}")
    return param


objekt = korutina(3)
print(type(korutina(3)))  # Ispisuje: <class 'coroutine'

async def main():
    print("pozvana main korutina...")
    await korutina(5)


asyncio.run(main())

"""


"""
import time

def fetch_data(paramatar):
    print(f"Delam nesto sa parametrom: {paramatar}")
    time.sleep(paramatar) 
    return f"Fetched data rezultat: {paramatar}"


def main():
    print("Izvrsavam main funkciju...")
    rezultat1 = fetch_data(2)
    rezultat2 = fetch_data(3)
    print("zavrsavam main funkciju")
    return rezultat1, rezultat2 #Tuple(string, string)

t1 = time.perf_counter()

main()

t2 = time.perf_counter()

print(f"Vreme izvrsavanja: {round(t2 - t1)} sekundi")

"""
"""
#primjer 2


import time, asyncio


async def fetch_data(paramatar):
    print(f"Delam nesto sa parametrom: {paramatar}")
    await asyncio.sleep(paramatar) 
    print(f"Zavsavam fetch_data funkciju")
    return f"Fetched data rezultat: {paramatar}"


async def main():
    print("Izvrsavam main funkciju...")
    task_1 = asyncio.create_task(fetch_data(2)) #schedule
    task_2 = asyncio.create_task(fetch_data(3))# schedule
    rezultat1 = await task_1 #run   
    rezultat2 = await task_2 #run
    print("zavrsavam main funkciju")
    return rezultat1, rezultat2 #Tuple(string, string)


asyncio.run(main())
t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vreme izvrsavanja: {round(t2 - t1)} sekundi")
"""

#primjer 3 
import time, asyncio


async def fetch_data(paramatar):
    print(f"Delam nesto sa parametrom: {paramatar}")
    await asyncio.sleep(paramatar) 
    print(f"Zavsavam fetch_data funkciju")
    return f"Fetched data rezultat: {paramatar}"


async def main():
    print("Izvrsavam main funkciju...")
    task_1 = asyncio.create_task(fetch_data(2)) #schedule
    task_2 = asyncio.create_task(fetch_data(3))# schedule


    
    rezultat1 = await task_2 #run   
    rezultat2 = await task_1 #run
    print("zavrsavam main funkciju")
    return rezultat1, rezultat2 #Tuple(string, string)


asyncio.run(main())
t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vreme izvrsavanja: {round(t2 - t1)} sekundi")