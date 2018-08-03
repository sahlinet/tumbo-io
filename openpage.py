def func(self):
	import requests, json
	r = requests.get("https://tumbo.io/")
	r1 = requests.get("https://tumbo.io/static/new_index.html")
	self.info(self.rid, "%s %s" % (r.status_code, r1.status_code))
	return self.responses.JSONResponse(json.dumps((r.status_code, r1.status_code)))