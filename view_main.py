def func(self):
	import sys, os
	import py_compile
	if self.request['REMOTE_ADDR'] == "127.0.0.1" and os.environ['EXECUTOR'] != "docker":
		sys.path.append("/Users/fatrix/Dropbox/Repositories/skyblue-cloud/app")
		py_compile.compile("/Users/fatrix/Dropbox/Repositories/tumbo-landingpage/app/index.py", doraise=True)
		import index
		reload(index)
	else:
		from app import index
	
	return index.func(self)