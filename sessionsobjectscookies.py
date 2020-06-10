#Python Program for Sessions, Cookies, Objects

import requests

s = requests.Session()
print(s.get('https://httpbin.org/cookies/set/sessioncookie/123456789'))
r = s.get('https://httpbin.org/cookies')
print('Text1 :: ', r.text)

print(s.get('https://httpbin.org/cookies/set/sessioncookie/helloworld'))
r = s.get('https://httpbin.org/cookies')
print('Text2 :: ', r.text)

#s.auth('user', 'pass')
#s.headers.update({'test':'true'})
r = s.get('https://httpbin.org/cookies', cookies={'from-my':'browser'})
print('Cookies text : ', r.text)

with requests.Session() as s:
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

r = requests.get('https://python.org')
print('Headers :: ', r.headers)
print('Request Headers : ', r.request.headers)

    
