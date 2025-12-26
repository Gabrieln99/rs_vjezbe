from aiohttp import web

async def kolicnik(request):
    try:
        data = await request.json()
        umnozak = data.get('umnozak')
        zbroj = data.get('zbroj')
        
        if umnozak is None or zbroj is None:
            return web.json_response(
                {'error': 'Umnožak i zbroj moraju biti proslijeđeni'},
                status=400
            )
        
        if zbroj == 0:
            return web.json_response(
                {'error': 'Dijeljenje s nulom nije dozvoljeno'},
                status=400
            )
        
        rezultat = umnozak / zbroj
        return web.json_response({'kolicnik': rezultat})
    
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

app = web.Application()
app.router.add_post('/kolicnik', kolicnik)

web.run_app(app, host='localhost', port=8085)
