def func(self):
	import requests
	r = requests.get("https://tumbo.io/")
	r1 = requests.get("https://tumbo.io/static/new_index.html")
	return r.status_code, r1.status_code