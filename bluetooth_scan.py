import bluetooth
from playsound import playsound

target_name = "Bluetooth speaker"
target_address = 'xx:xx:xx:xx' # bluetooth address
# bdaddr = 'xx:xx:xx:xx'

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None :
    #print ("found target bluetooth device with address ", target_address)
    #print (target_name, ':', target_address)
    playsound('xxx.mp3') # the path of voice or music 
    
else:
    print ("there is no bluetooth speaker nearby")
