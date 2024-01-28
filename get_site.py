from netbox import NetBox 
netbox = NetBox(host='10.1.30.100', port=80, use_ssl=False, auth_token='fba61fd21c401c7af1c67a565924025de024781c')

nb_sites = netbox.dcim.get_sites()
print(nb_sites)
