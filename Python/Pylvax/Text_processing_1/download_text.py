import requests

r = requests.get('http://paste.ee/r/DPASQ')

source = open ('source_file.txt', 'w') 
source.write(r.text)
source.close()