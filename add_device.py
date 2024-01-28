import pynetbox
#import time

dev = "R1"

def adddev(dev):
    nb = pynetbox.api(url='https://10.1.30.100/',
                      token='fba61fd21c401c7af1c67a565924025de024781c')
    nb.http_session.verify = False


    result = nb.dcim.devices.create(
        name=dev,
        device_type=2,
        device_role=2,
        device_manufacturer=7,
        site=3,
    )
    print(result)
    
adddev(dev)