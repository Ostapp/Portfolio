import requests
import json
from time import strftime
from datetime import datetime

r = requests.get('https://api.forecast.io/forecast/dd7278d70bf285fe1a9d0cd33cc59ccb/52.5167,13.3833?units=si')
d_txt = json.loads(r.text)

data_list = d_txt['daily']['data']
output_d = {}
output_l = []

i = 0
while i < 8:
    for item in data_list:
            output_d[data_list[i]['temperatureMax']] = datetime.fromtimestamp(data_list[i]['time']).strftime('%Y-%m-%d %H:%M:%S')
            output_l.append(output_d)
            i = i+1
	

print(output_l)

    
    
