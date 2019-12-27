import json
import requests
baseurl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc':'0885909950805'}
response = requests.get(baseurl,params=parameters)
print(response.url)
content = response.content
info = json.loads(content)
#print(type(info))
#print(info)
item = info['items']
iteminfo = item[0]
#print(iteminfo)
title = iteminfo['title']
brand = iteminfo['brand']
print(title)
print(brand)
