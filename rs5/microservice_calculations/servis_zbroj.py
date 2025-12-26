from aiohttp import web

async def zbroj(request):
    try:
        data = await request.json()
        brojevi = data.get('brojevi')
        
        if not brojevi or not isinstance(brojevi, list):
            return web.json_response(
                {'error': 'Lista brojeva nije proslijeđena'},
                status=400
            )
        
        rezultat = sum(brojevi)
        return web.json_response({'zbroj': rezultat})
    
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

app = web.Application()
app.router.add_post('/zbroj', zbroj)

web.run_app(app, host='localhost', port=8083)
