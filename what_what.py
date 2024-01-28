import requests
import json

url = "http://10.1.30.100/api/dcim/devices"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token 4fbaf8e5272978b3ef7ff12a35b6746e1154f072'
}


response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)