#Python Program for Soap request

import requests,bs4

result = requests.get('http://mas.bg.ac.rs')
#result.text

SiteSoup = bs4.BeautifulSoup(result.text)
elements = SiteSoup.select('div')
len(elements)

