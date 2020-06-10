#Python Program for JSON

import json
import requests

r = requests.get('https://httpbin.org/stream/20', stream=True)
##for line in r.iter_lines():
##    if line:
##            decoded_line = line.decode('utf-8')
##            #print(json)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    if line:
        print(json.load(line))
