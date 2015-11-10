__author__ = 'techbk'


import requests

class HTTPClient(object):
    def __init__(self, base_url, token=None, project_id=None, user_id=None):
        self.base_url = base_url
        self.token = token
        self.project_id = project_id
        self.user_id = user_id


    def get(self, url, headers=None):
        headers = self._update_headers(headers)

        return requests.get(self.base_url + url, headers=headers)


    def post(self, url, body, headers=None, file = None):
        headers = self._update_headers(headers)
        content_type = headers.get('content-type', 'application/json')
        headers['content-type'] = content_type

        return requests.post(self.base_url + url, body, headers=headers, file = file)


    def put(self, url, body, headers=None):
        headers = self._update_headers(headers)
        content_type = headers.get('content-type', 'application/json')
        headers['content-type'] = content_type

        return requests.put(self.base_url + url, body, headers=headers)


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

class My_HttpClient(HTTPClient):

    def post_file(self, url, headers=None, files = None):
        headers = self._update_headers(headers)
        return requests.post(self.base_url + url, headers=headers, files = files)


if __name__ == "__main__":
    import client
    http_client = HTTPClient(client.HORIZON_URL)
    r = http_client.post('/post')
    print r.headers
    print r.text