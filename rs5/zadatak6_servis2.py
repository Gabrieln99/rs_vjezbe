from aiohttp import web
import asyncio

async def pozdrav(request):
    await asyncio.sleep(4)
    return web.json_response({"message": "Pozdrav nakon 4 sekunde"})

app = web.Application()
app.router.add_get('/pozdrav', pozdrav)

web.run_app(app, host='localhost', port=8082)
