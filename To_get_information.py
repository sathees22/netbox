import requests

from rich import print as r_print 

headers = {"authorization": "Token 9fecfd7d2aac1259a65a557c77d512c65c1a5c57"}

response = requests.get("https://10.1.30.100/api/dcim/devices", headers=headers, verify=False)

r_print(response.json())
