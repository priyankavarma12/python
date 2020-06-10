#Python Program for http://httpbin/org/get data

import requests

r = requests.get('http://httpbin.org/get')
print(r.headers['Server'])
print(r.headers['Date'])
print(r.headers['Content-Type'])

response =  r.json()
print(r.json())
print('URL ::  ', response['url'])

payload = {'username':'admin', 'password':'password'}
r = requests.get('http://httpbin.org/get', params=payload)
print('Text :: ', r.text)
