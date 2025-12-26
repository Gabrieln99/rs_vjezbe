import asyncio
import aiohttp

async def dohvati_cinjenice(session, amount):
    async with session.get(f'http://localhost:8086/cats/{amount}') as response:
        return await response.json()

async def filtriraj_cinjenice(session, facts):
    async with session.post('http://localhost:8087/facts', json={'facts': facts}) as response:
        return await response.json()

async def main():
    broj_cinjenica = 10
    print(f"Dohvacam {broj_cinjenica} cinjenica o mackama...\n")
    
    async with aiohttp.ClientSession() as session:
        print("=== DOHVACANJE CINJENICA (mikroservis 1) ===")
        rezultat1 = await dohvati_cinjenice(session, broj_cinjenica)
        
        print(f"Dohvaceno {rezultat1['count']} cinjenica:")
        for i, fact in enumerate(rezultat1['facts'], 1):
            print(f"  {i}. {fact[:80]}...")
  
        print(f"\n=== FILTRIRANJE CINJENICA (mikroservis 2) ===")
        rezultat2 = await filtriraj_cinjenice(session, rezultat1['facts'])
        
        print(f"Od {rezultat2['original_count']} cinjenica, {rezultat2['filtered_count']} sadrzi 'cat' ili 'cats':")
        for i, fact in enumerate(rezultat2['filtered_facts'], 1):
            print(f"  {i}. {fact[:80]}...")

asyncio.run(main())
