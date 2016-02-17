from bottle import route, run, template
from GeoNames import *

url_template = 'https://api.forecast.io/forecast/{api}/{lat},{lon}'
apikey = 'dd7278d70bf285fe1a9d0cd33cc59ccb'
latitude = 47.53
longitude = 19.05
username = "ostap"


@route('/')
@route('/hello/<name>')
@route('/hello/<name>/<width>')
def greet(name='Stranger', width=300):
	return template('Hello {{name}}, <img src ="http://polomania.hu/images/designs/tn3/1987904494512cb7497ee46.jpg" width={{width}}> how are you?', name=name, width=width)


@route('/sq/<number>')
def sq(number):
	number = float(number) #convert from str to number
	return str(number**2) #and convert back to 
	

@route('/palindrom/<word>')
def is_palinfrom(word):
	result = word == word[::-1]
	return str(result)


@route('temp/<lat>/<lon>')
def temperature_lat_lon(lat,lon):
	lat = float(lat)
	lon = float(lon)
	url = url_template.format(api=apikey, lat=latitude, lon=longitude)
	params_dict = {
		'units':'si'
	}

	r = r.requests.get(url, params=params_dict)
	if not r.ok:
		return 'error'

	data = r.json()
	temp = data['currently']['temperature']
	return temp

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

# def getCityLanLonByName (name):

# 	global username

# 	url_template_geoNames = 'http://api.geonames.org/searchJSON?name_equals={name}&username={username}'

# 	url_geoNames = url_template_geoNames.format(name=name, username=username)

# 	r = requests.get(url_geoNames)

# 	if not r.ok:
# 		return 'error'

# 	data = r.json()

# 	lat = data['geonames'][0]['lat']
# 	lon = data['geonames'][0]['lng']
	
# 	return lat,lon


# do the same with city names
# check maphub.net
# geocoding/ reverse geocoding
# do geocoding using 

run(host='localhost', port=8080, debug=True)	