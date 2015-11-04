import asyncio
from aiohttp import web

async def hello(request):
    return web.Response(body=b"Hello, world")

app = web.Application
# app = web.Application()
app.router.add_route('GET', '/', hello)
loop = asyncio.get_event_loop()
handler = app.make_handler()
f = loop.create_server(handler,'0.0.0.0',8000)
srv = loop.run_until_complete(f)
