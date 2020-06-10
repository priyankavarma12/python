#Python Program for HTTP Get Request

import requests

r = requests.get('https://facebook.com')
print(r.content)
