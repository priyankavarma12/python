#Python Program for Authentication

from requests.auth import AuthBase
class CustomAuth(AuthBase):
    def __init__(self, username):
            self.usernmae = username
    def __call__(self, r):
            r.headers['Our-Custom-Auth'] = self.username
            return r

import requests
print(requests.get('http://arh.bg.ac.rs', auth=CustomAuth('admin')))

    
