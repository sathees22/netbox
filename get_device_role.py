from netbox import NetBox 
netbox = NetBox(host='10.1.30.100', port=80, use_ssl=False, auth_token='fba61fd21c401c7af1c67a565924025de024781c')

nb_device_roles  = netbox.dcim.get_device_roles()
print(nb_device_roles)