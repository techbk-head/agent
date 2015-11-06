__author__ = 'techbk'


import requests

#import logging


#LOG = logging.getLogger(__name__)


#def log_request(func):
    #def decorator(self, *args, **kwargs):
        #resp = func(self, *args, **kwargs)
        #LOG.debug("HTTP %s %s %d" % (resp.request.method, resp.url,
                  #resp.status_code))
        #return resp
    #return decorator


class HTTPClient(object):
    def __init__(self, base_url, token=None, project_id=None, user_id=None):
        self.base_url = base_url
        self.token = token
        self.project_id = project_id
        self.user_id = user_id

    #@log_request
    def getHeader(self, url, headers=None):
        headers = self._update_headers(headers)
        print headers
        return requests.get(self.base_url + url, headers=headers)


    #@log_request
    def get(self, url, headers=None):
        headers = self._update_headers(headers)

        return requests.get(self.base_url + url, headers=headers)

    #@log_request
    def post(self, url, body, headers=None, file = None):
        headers = self._update_headers(headers)
        content_type = headers.get('content-type', 'application/json')
        headers['content-type'] = content_type

        return requests.post(self.base_url + url, body, headers=headers, file = file)

    #@log_request
    def put(self, url, body, headers=None):
        headers = self._update_headers(headers)
        content_type = headers.get('content-type', 'application/json')
        headers['content-type'] = content_type

        return requests.put(self.base_url + url, body, headers=headers)

    #@log_request
    def delete(self, url, headers=None):
        headers = self._update_headers(headers)

        return requests.delete(self.base_url + url, headers=headers)

    def _update_headers(self, headers):
        if not headers:
            headers = {}

        token = headers.get('x-auth-token', self.token)
        if token:
            headers['x-auth-token'] = token

        project_id = headers.get('X-Project-Id', self.project_id)
        if project_id:
            headers['X-Project-Id'] = project_id

        user_id = headers.get('X-User-Id', self.user_id)
        if user_id:
            headers['X-User-Id'] = user_id

        return headers

if __name__ == "__main__":
    import client
    http_client = HTTPClient(client.HORIZON_URL)
    r = http_client.post('/post')
    print r.headers
    print r.text