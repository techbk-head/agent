__author__ = 'techbk'

# Copyright 2014 - Mirantis, Inc.
# Copyright 2015 - StackStorm, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

#import six

from old__htmlclient import My_HttpClient

#HORIZON_URL = 'http://192.168.145.131/admin/'
#HORIZON_URL = 'http://httpbin.org'
HORIZON_URL = 'http://0.0.0.0:8877'
SERVICE_URL = 'http://0.0.0.0:8080'
AUTH_URL = "http://192.168.145.131:5000/v2.0"


class Client(object):
    def __init__(self, horizon_url=None, username=None, api_key=None,
                 project_name=None, auth_url=None, project_id=None,
                 endpoint_type='publicURL', service_type=None,
                 auth_token=None, user_id=None, cacert=None):

        #if mistral_url and not isinstance(mistral_url, six.string_types):
            #raise RuntimeError('Mistral url should be string')

        if auth_url:
            (auth_token, project_id, user_id) = (
                self.authenticate(username, api_key,
                                  project_name, auth_url, project_id,
                                  endpoint_type, service_type, auth_token,
                                  user_id, cacert))

        if not horizon_url:
            horizon_url = SERVICE_URL

        self.http_client = My_HttpClient(horizon_url,
                                                 auth_token,
                                                 project_id,
                                                 user_id)


    def authenticate(self, username=None, api_key=None,
                     project_name=None, auth_url=None, project_id=None,
                     endpoint_type='publicURL', service_type=None,
                     auth_token=None, user_id=None, cacert=None):

        if project_name and project_id:
            raise RuntimeError('Only project name or '
                               'project id should be set')

        if username and user_id:
            raise RuntimeError('Only user name or user id'
                               ' should be set')

        keystone_client = _get_keystone_client(auth_url)

        keystone = keystone_client.Client(
            username=username,
            user_id=user_id,
            password=api_key,
            token=auth_token,
            tenant_id=project_id,
            tenant_name=project_name,
            auth_url=auth_url,
            endpoint=auth_url,
            cacert=cacert)

        keystone.authenticate()
        token = keystone.auth_token
        user_id = keystone.user_id
        project_id = keystone.project_id

        #if not horizon_url:
            #catalog = keystone.service_catalog.get_endpoints(
                #service_type=service_type,
                #endpoint_type=endpoint_type
            #)
            #if service_type in catalog:
                #service = catalog.get(service_type)
                #horizon_url = service[0].get(
                    #endpoint_type) if service else None
        print token
        return token, project_id, user_id


def _get_keystone_client(auth_url):
    if "v2.0" in auth_url:
        from keystoneclient.v2_0 import client
    else:
        from keystoneclient.v3 import client

    return client


if __name__ == "__main__":
    client = Client(username='admin', api_key='baogavn' ,auth_url=AUTH_URL, project_name='admin')
    #r = client.http_client.get('/headers')
    files = {'file':( 'a.pcap',open('pcap/a.pcap', 'rb'), 'application/json')}
    r = client.http_client.post_file(url='/pcap',files=files)
    #r = client.http_client.post_file(url='/techbk_head/list/',files=files)
    #r = client.http_client.get(url='/techbk_head/list/')

    print r.text
    print r.headers
    print r.url
    print r.status_code