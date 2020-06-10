#Python Program for POST http request

import requests

payload = {'username':'admin', 'password':'password'}
r = requests.post('http://httpbin.org/post', data=payload)
print('URL - ', r.url)
print('Text : ', r.text)


r = requests.post('http://www.github.com')
print('History :: ', r.history)
print('Status Code ::', r.status_code)

r = requests.post('http://www.github.com', allow_redirects=False)
print(r.history)

