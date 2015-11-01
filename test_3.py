__author__ = 'techbk'

import aiohttp
import asyncio

@asyncio.coroutine
def fetch(client):
    #async with client.get('http://python.org') as resp:
    resp = yield from client.get('http://python.org')
    #assert resp.status == 200
    t = yield from resp.text()
    print(t)

with aiohttp.ClientSession() as client:
    asyncio.get_event_loop().run_until_complete(fetch(client))