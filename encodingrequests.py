#Python Program for Encoding in requests

import requests

r = requests.get('https://api.github.com/events')
print('Text :: ', r.text)

print('Encoding :: ', r.encoding)

print('Content :: ', r.content)

result = requests.get('https://api.github.com/events', stream=True)
print('Raw :: ', r.raw)

print('reading of lines ', r.raw.read(10))
print('Raw of result', result.raw.read(10))

url = 'https://httpbin.org/post'
files = {'file': open('C://Users//Priyanka_Varma//AppData//Local//Programs//Python//Python38-32//webbrowseropen.py', 'rb')}

result = requests.post(url, files=files)


print(r.text)

print("content of webbrowser file :: ", result.text)
