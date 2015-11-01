__author__ = 'techbk'

import asyncio
import aiohttp



@asyncio.coroutine
def as_get():
    payload = {'key1': 'value1', 'key2': 'value2'}
    #async with aiohttp.get('http://httpbin.org/get',
                           #params=payload) as r:
    r = yield from aiohttp.get('http://httpbin.org/get',params=payload)
    t = yield from r.text()
    #t = yield from r.read()
    print(t)

loop = asyncio.get_event_loop()

loop.run_until_complete(as_get())