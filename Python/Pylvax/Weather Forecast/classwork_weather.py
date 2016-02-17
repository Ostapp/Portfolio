import requests
import json

s = 'valami {a}, something {b}'
s.format(a=1,b=5)

# lookup format module

longitude = '52.5167'
latitude = '13.3833'

#units = 'units=si'

url_template = 'https://api.forecast.io/forecast/{api}/{lat},{lon}'

apikey = 'dd7278d70bf285fe1a9d0cd33cc59ccb'

#lang = 'lang=de'

params_dict={'units': 'si', 'lang': 'de'}

url = url_template.format(api=apikey, lat=latitude, lon=longitude)r

r = requests.get(url, params_dict)

# r = requests.get(url + '?units=si')

data = json.loads(r.text)

print(type(data), type(data['daily']), type(data['daily']['data']))

# print



# jsonview chrome extension is good for looking at json files

