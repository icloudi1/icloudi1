import requests
import json
baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
paramters = {'q':'Khartoum,SD','APPID':'bfc6f801393f5556f158705b0a2a2b29'}
response = requests.get(baseUrl,params=paramters)
print(response.content)
info = json.loads(response.content)
store = info['coord']
storeInfo = store[1]
product = storeInfo['lon']
print(product)
 