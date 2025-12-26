import asyncio
import aiohttp
import time

async def dohvati_pozdrav(url, port):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{url}:{port}/pozdrav") as response:
            return await response.json()

async def main():
    print("=== SEKVENCIJALNO ===")
    start = time.time()
    
    odgovor1 = await dohvati_pozdrav("localhost", 8081)
    print(f"Servis 1: {odgovor1}")
    
    odgovor2 = await dohvati_pozdrav("localhost", 8082)
    print(f"Servis 2: {odgovor2}")
    
    print(f"Sekvencijalno vrijeme: {time.time() - start:.2f}s\n")
    
 
    print("=== KONKURENTNO ===")
    start = time.time()
    
    odgovori = await asyncio.gather(
        dohvati_pozdrav("localhost", 8081),
        dohvati_pozdrav("localhost", 8082)
    )
    
    print(f"Servis 1: {odgovori[0]}")
    print(f"Servis 2: {odgovori[1]}")
    print(f"Konkurentno vrijeme: {time.time() - start:.2f}s")

asyncio.run(main())
