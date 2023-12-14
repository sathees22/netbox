import requests
import json

url = "https://10.1.30.100/api/dcim/devices"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token 81f86392c51605271ce7c9564d72534b85b40b6e'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
