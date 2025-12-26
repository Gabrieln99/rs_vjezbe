from aiohttp import web
import aiohttp
import asyncio

CAT_FACT_API = "https://catfact.ninja/fact"

async def dohvati_jednu_cinjenicu(session):
    async with session.get(CAT_FACT_API) as response:
        data = await response.json()
        return data.get('fact')

async def get_cats(request):
    try:
        amount = int(request.match_info['amount'])
        
        if amount <= 0:
            return web.json_response(
                {'error': 'Broj činjenica mora biti veći od 0'},
                status=400
            )
        
        async with aiohttp.ClientSession() as session:
            # Konkurentno dohvaćanje činjenica
            tasks = [dohvati_jednu_cinjenicu(session) for _ in range(amount)]
            cinjenice = await asyncio.gather(*tasks)
        
        return web.json_response({'facts': cinjenice, 'count': len(cinjenice)})
    
    except ValueError:
        return web.json_response({'error': 'Neispravan broj'}, status=400)
    except Exception as e:
        return web.json_response({'error': str(e)}, status=500)

app = web.Application()
app.router.add_get('/cats/{amount}', get_cats)

web.run_app(app, host='localhost', port=8086)
