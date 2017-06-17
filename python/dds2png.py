import json, requests, shutil

url = 'http://api.rest7.com/v1/image_convert.php?format=png'
files = {'file': ('test.dds', open('test.dds', 'rb'), 'application/octet-stream', {'Expires': '0'})}

js = requests.post(url, files=files).text
data = json.loads(js)
if (data['success'] != 1):
	print('Conversion failed')
else:
	image = requests.get(data['file'], stream=True).raw
	with open('output.png', 'wb') as f:
		shutil.copyfileobj(image, f)

