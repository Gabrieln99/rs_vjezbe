from aiohttp import web

proizvodi = [
    {"naziv": "Laptop", "cijena": 1200, "kolicina": 5},
    {"naziv": "Mis", "cijena": 25, "kolicina": 20}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def post_proizvodi(request):
    data = await request.json()
    print("Primljen proizvod:", data)

    proizvodi.append(data)
    return web.json_response(proizvodi)

app = web.Application()

app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_post('/proizvodi', post_proizvodi)

web.run_app(app, host='localhost', port=8081)

