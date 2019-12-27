import requests
baseURL='http://api.openweathermap.org/data/2.5/weather'
parameters = {'APPID': 'c5afeec3c0a0bc630c4864146dbaf31a','q':'London,uk'}
response = requests.get(baseURL, params=parameters)
print(response.content)
