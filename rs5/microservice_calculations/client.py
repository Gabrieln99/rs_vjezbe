import asyncio
import aiohttp

async def pozovi_zbroj(session, brojevi):
    async with session.post('http://localhost:8083/zbroj', json={'brojevi': brojevi}) as response:
        return await response.json()

async def pozovi_umnozak(session, brojevi):
    async with session.post('http://localhost:8087/umnozak', json={'brojevi': brojevi}) as response:
        return await response.json()

async def pozovi_kolicnik(session, umnozak, zbroj):
    async with session.post('http://localhost:8085/kolicnik', json={'umnozak': umnozak, 'zbroj': zbroj}) as response:
        return await response.json()

async def main():
    brojevi = [2, 3, 4, 5]
    print(f"Brojevi: {brojevi}\n")
    
    async with aiohttp.ClientSession() as session:

        print("=== KONKURENTNO: zbroj i umnožak ===")
        rezultati = await asyncio.gather(
            pozovi_zbroj(session, brojevi),
            pozovi_umnozak(session, brojevi)
        )
        
        zbroj_rezultat = rezultati[0]
        umnozak_rezultat = rezultati[1]
        
        print(f"Zbroj: {zbroj_rezultat}")
        print(f"Umnozak: {umnozak_rezultat}\n")
     
        print("=== SEKVENCIJALNO: kolicnik ===")
        kolicnik_rezultat = await pozovi_kolicnik(
            session,
            umnozak_rezultat['umnozak'],
            zbroj_rezultat['zbroj']
        )
        print(f"Količnik (umnozak/zbroj): {kolicnik_rezultat}")

asyncio.run(main())
