from aiohttp import web

async def filter_facts(request):
    try:
        data = await request.json()
        facts = data.get('facts')
        
        if not facts or not isinstance(facts, list):
            return web.json_response(
                {'error': 'Lista činjenica nije proslijeđena'},
                status=400
            )
        
        filtered_facts = [
            fact for fact in facts 
            if 'cat' in fact.lower() or 'cats' in fact.lower()
        ]
        
        return web.json_response({
            'filtered_facts': filtered_facts,
            'original_count': len(facts),
            'filtered_count': len(filtered_facts)
        })
    
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

app = web.Application()
app.router.add_post('/facts', filter_facts)

web.run_app(app, host='localhost', port=8087)
