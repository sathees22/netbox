
import pynetbox
nb = pynetbox.api(url="http://10.1.30.100/", token="fba61fd21c401c7af1c67a565924025de024781c")
nb.http_session.verify = False

x = nb.dcim.devices.get(6)
print(x)

y = nb.dcim.devices_types.get(2)
print(y)