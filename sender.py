import requests
import json
url = 'http://127.0.0.1:5000/work'
dns='http://test.eric-n.com/work'
ip='http://10.10.100.198:5000/work'
data = { 'name': 'freshdesk-auth-tool', 
         'message': 'test message' }


data2 = { 'name': 'create VM', 
         'message': 'test message' }


def sendPOST(url,message):
    print("Sending to "+url,end=" - ")
    r = requests.post(url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
    print(r.status_code)

sendPOST(url,data)
sendPOST(dns,data)
sendPOST(ip,data)
