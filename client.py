__author__ = 'techbk'
# class gui file pcap

#from old__htmlclient import My_HttpClient

import requests
import config
import json



class HTTPClient(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, url, data=None, headers=None, files = None, json = None):
        #headers = self._update_headers(headers)
        if headers:
            content_type = headers.get('content-type', 'application/json; charset=utf-8')
            headers['content-type'] = content_type

        return requests.post(self.base_url + url, data=data, headers=headers, files = files, json = json)




class Client(object):
    def __init__(self, base_url=None,data=None,dump_json=True):

        if not base_url:
            base_url = config.SERVICE_URL

        if not data:
            data = {'ID_Client':config.LOCAL_NAME}

        self._dump_json=dump_json
        self._data=data
        self.http_client = HTTPClient(base_url)

    def loop(self,data=None):
        #while True:
            #if self._has_new_file():
                return self._send_file(data)

    def _send_file(self,data):
        if self._dump_json:
            if not data:
                data = self._data
                print(data)
        #data = json.dumps(data)
        #print(data)
        #resp = self.client.http_client.post(url, data)
        files = {'file':( 'a.pcap',open('pcap/a.pcap', 'rb'), 'application/json')}
        return self.http_client.post(url='/pcap', files=files, json = data)


if __name__ == "__main__":
    client = Client()
    r = client.loop()
    print "################"
    print r.text
    print r.headers
    print r.url
    print r.status_code