import requests
import json

url = "http://10.1.30.100/api/dcim/devices/"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token 4fbaf8e5272978b3ef7ff12a35b6746e1154f072'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
json_data = response.json()


#print(response.text.encode('utf8'))
results = json_data['results']
      
for device in results:
      hostname = device['name']
      #type = device['type']      
      #ipaddr = device['primary_ip']['address']
      print('The IP address of  ' + hostname + ' is '  )
