def func(self):
	import time
	import requests
	
	time.sleep(0.2)
	
	r = requests.get("https://planet-lite-test.sahli.net/fastapp/api/base/tumbo-landingpage/apy/empty/execute/?json=&async", headers={'Authorization': "TOKEN 7bcd9e37991e0932d1f89b6e7d993851102fffb4"})
	
	time.sleep(5)
	
	url = r.json()['url']
	r1 = requests.get("https://planet-lite-test.sahli.net"+url, headers={'Authorization': "TOKEN 7bcd9e37991e0932d1f89b6e7d993851102fffb4"})
	
	
	return r1.json()['returned']