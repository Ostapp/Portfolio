from bottle import route, run, template
from GeoNames import *

# for forecast.io API
url_template = 'https://api.forecast.io/forecast/{api}/{lat},{lon}'
apikey = 'dd7278d70bf285fe1a9d0cd33cc59ccb'

# check temperature by latitude/longitude
@route('temp/<lat>/<lon>')
def temperature_lat_lon(lat,lon):
	
	lat = float(lat)
	lon = float(lon)
	url = url_template.format(api=apikey, lat=latitude, lon=longitude)
	params_dict = {
		'units':'si'
	}

	r = requests.get(url, params=params_dict)
	if not r.ok:
		return 'error'

	data = r.json()
	temp = data['currently']['temperature']

	return str(temp)

# check temperature by city Name 
@route('temp/<cityName>')
def temperature_city(cityName):

	lat,lon = getCityByName(cityName)

	lat = float(lat)
	lon = float(lon)

	url = url_template.format(api=apikey,lat=lat, lon=lon)

	params_dict = {'units':'si'}

	r = requests.get(url, params=params_dict)

	if not r.ok:
		return 'error'

	data = r.json()
	temp = data['currently']['temperature']

	return str(temp)


run(host='localhost', port=8080, debug=True)	