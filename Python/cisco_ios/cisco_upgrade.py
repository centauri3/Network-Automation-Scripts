from netmiko import ConnectHandler
import getpass

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '',
    'username': 'admin',
    'password': getpass,
    'secret': ''
}

ssh = ConnectHandler(**cisco_router)

image = ""
direction = "put"


#Print out current version
ver = ['show version']
out = ssh.send_command(ver)
print(out)

with open(out) as openfile:
    for line in openfile:
        line = line.strip()
        if "version" in line:
            print('The version is: ')


#SCP The File To The Device
