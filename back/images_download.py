import requests

def download(url, name):
	print("download : ")
	print(url)
	print(name)
	img_data = requests.get(url).content
	with open(name, 'wb') as handler:
	    handler.write(img_data)
