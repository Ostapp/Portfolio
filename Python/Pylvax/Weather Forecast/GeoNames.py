import requests

username = "ostap"

def getCityByName (name):

	global username

	url_template_geoNames = 'http://api.geonames.org/searchJSON?name_equals={name}&username={username}'

	url_geoNames = url_template_geoNames.format(name=name, username=username)

	r = requests.get(url_geoNames)

	if not r.ok:
		return 'error'

	data = r.json()

	lat = data['geonames'][0]['lat']
	lon = data['geonames'][0]['lng']
	
	return lat,lon


