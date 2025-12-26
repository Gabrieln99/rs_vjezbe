from aiohttp import web

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 999.99, "kolicina": 10},
    {"id": 2, "naziv": "Miš", "cijena": 29.99, "kolicina": 50},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 79.99, "kolicina": 30},
    {"id": 4, "naziv": "Monitor", "cijena": 299.99, "kolicina": 15}
]


async def get_proizvodi(request):
    return web.json_response(proizvodi)


async def get_proizvod_by_id(request):
    proizvod_id = int(request.match_info['id'])
    
    for p in proizvodi:
        if p['id'] == proizvod_id:
            return web.json_response(p)
    
    return web.json_response(
        {'error': 'Proizvod s traženim ID-em ne postoji'},
        status=404
    )

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)

web.run_app(app, host='localhost', port=8081)
