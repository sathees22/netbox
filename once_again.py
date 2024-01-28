
import requests
from rich import print as r_print

# Headers for the API request
headers = {"Authorization": "Token 9fecfd7d2aac1259a65a557c77d512c65c1a5c57"}
device_type = "dcim/device-types/" #id': 2
device_role = "dcim/device-roles/" #id': 1
sites = "dcim/sites/" #id': 3
devices = "dcim/devices/"
url = 'https://10.1.30.100/api/'

ip_address = "ipam/ip-address/"
tenent_api =  "tenancy/tenants/"
manufacturer = "dcim/manufacturers/"
rack = "dcim/racks/"
response = requests.get(url + tenent_api, headers=headers, verify=False)

''' for each_line in response.json()["results"]:
    r_print(each_line)

exit()  '''   

data_payload = {
    "name" : "SK05",
    "device_type": {
        "id" : 2,
    },
    "role" : {
        "id" : 1,
    },
    "site" : {
        "id" : 3,
    },
    
    "tenant" : {
        "id" :7,
    },
    "serial" : "test220471"
    
}

response = requests.post(url + devices, headers=headers, verify= False, json=data_payload)

r_print(response)