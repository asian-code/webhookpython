import requests
import json
url = 'http://127.0.0.1:5000/home'
url2="http://127.0.0.1:5000/freshdesk"
data = { 'name': 'Testing name data', 
         'message': 'message' }

r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})



