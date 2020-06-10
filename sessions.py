#Python program for Sessions

from requests import Request, Session

s = Session()
req = Request('POST', 'https://python.org')
prepped =  req.prepare()
print(prepped)

 

### SSL Certificates and Authentications
import requests

s = requests.Session()
s.verify = '/path/to/certificate'
#requests.get('https://github.com', verify=False)

url = 'https://twitter.com'
r = requests.get(url, stream=True)
if int(r.headers['content-length']) < TOO_LONG:
    content = r.content
    print(r.content)
