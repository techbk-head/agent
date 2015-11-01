__author__ = 'techbk'

import asyncio
import aiohttp

@asyncio.coroutine
def fetch_page(client, url):
    response = yield from client.get(url)
    assert response.status == 200
    #result = yield from response.read()
    text = yield from response.text()
    return text

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)
content = loop.run_until_complete(fetch_page(client, 'https://api.github.com/events'))
print(content)
client.close()