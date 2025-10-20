#Completion Status: WIP
#Date: 10/20/2025
#Git: True

from netmiko import ConnectHandler
from deviceInventory import PErouters
from getpass import getpass

# A way to connect to devices. I added a list for host which is imported form the deviceInventory file for better organization of devices.
net_connect = ConnectHandler(
    device_type = "cisco",
    host = PErouters,
    username = "",
    password = getpass()
)

controlPLaneVerification = [
    'show mpls ldp discovery',
    'show mpls ldp neighbor',
    'show forwarding-table',
    'show ip route mpls',
]

showCommandExecute = net_connect.send_config_set

for answer in input('Do you want to perform a traceroute? (Yes, Y, No, N)\n'):
    if answer is("Yes" or 'Y'):
        destinationIP = input('Enter the destination IP: ')
        tracerouteOutput = net_connect.send_command(f'traceroute mpls {destinationIP}')
        print(tracerouteOutput)
    elif answer is 'No' or 'N':
        print("You have chosen to not perform a traceroute. Skipping.")
        continue
    else:
        print("You have chosen a answer that is not valid.")

showL3VPNConnections = ()


print(f"Type of output: {type(showCommandExecute)}")
print("---Device Output---")
print(showCommandExecute)