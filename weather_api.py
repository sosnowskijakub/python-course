import requests

city = 'Krakow'
url = requests.get('http://api.weatherapi.com/v1/current.json?key=9c0e0fd645f74f0ab17190029230912&q='+city+'&aqi=no')
weather_json = url.json()
temp = weather_json.get('current').get('temp_c')
conditions = weather_json.get('current').get('condition').get('text')

print('The current weather in', city, 'is:', temp, "celcius degrees and condtion is", conditions)
