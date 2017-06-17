from urllib.request import urlopen
import json

ip = '167.187.101.241';
f = urlopen('http://api.rest7.com/v1/ip_to_city.php?ip=' + ip)
js = f.read().decode('utf-8')
data = json.loads(js)
if (data['success'] != 1):
	print('Failed')
else:
	print('Country=' + data['country'] + "\r\n" +
			'Region=' + data['region']  + "\r\n" +
			'City=' + data['city']  + "\r\n" +
			'Latitude=' + data['lat']  + "\r\n" +
			'Longitude=' + data['lng']);