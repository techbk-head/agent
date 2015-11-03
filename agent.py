__author__ = 'techbk'

import asyncio
import aiohttp

URL = 'http://httpbin.org/post'

class manager_pcap_file:

    def __init__(self,client):
        self.__client == client


    @asyncio.coroutine
    def send_file_pcap(self,f):
        data = FormData()
        data.add_field('file',
               open(f, 'rb'),
               filename=f
               )
        yield from aiohttp.post(url, data=data)

    def __newfile(self):
        #check new file

        return True

    @asyncio.coroutine
    def main(self):
        while True:
            f = self.__newfile()
            if f:
                yield from send_file_pcap(f)

@asyncio.coroutine
def manager_pcap():

@asyncio.coroutine
def main(loop):
    with aiohttp.ClientSession() as client:
        manager_p_f = manager_pcap_file(client)
        asyncio.async(manager_p_f.main())
    asyncio.async(manager_pcap())


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass


