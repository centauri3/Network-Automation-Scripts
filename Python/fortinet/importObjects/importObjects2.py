import pandas as pd
from getpass import getpass
#import pyfortiapi
#import requests

'''
#Editable Variables
forti_ip = 10.10.10.10
username = input("Enter username: ")
password = getpass("Enter password: ")

#Variables passed over to login to a device
device = pyfortiapi.FortiGate(ipaddr=forti_ip,
                                  username=username,
                                  password=password,
                                  vdom="Prod")
'''

#if located within another directory. COMMENT OUT IF IN THE SAME DIRECTORY.
workbook_path = r"C:\Users\devih\Documents\Git\Automation\Python\fortinet\file.xlsx"

#Enter the workbook variable or file name
workbook = pd.read_excel(workbook_path, sheet_name="Firewall Objects")

##Importing Objects

# Iterate through each row in the DataFrame
for index, row in workbook.iterrows():
    # Extract policy information from the current row
    if row['Reason'] == 'Create':
        excel_data = {
            'name': row['Device'],
            'reason': row['Reason'],
            'change_description': row['Change Description'],
            'type': row['Object Type'],
            'member': row['Object Address/Service/Group'],
            'subnet': row['Source Address/Member'],
            'description': row['Comment/Description']
        }
    
    #####print(excel_data)######
    
    #bundle dict into a payload
        object_payload = {key: excel_data[key] for key in excel_data.keys() & {'name', 'type', 'subnet', 'description'}}
    
    #####print(object_payload)
    
        device.create_firewall_address(object_payload)
        break
    
    elif row['Reason'] == 'Modify':
        excel_data = {
            'name': row['Device'],
            'reason': row['Reason'],
            'change_description': row['Change Description'],
            'type': row['Object Type'],
            'member': row['Object Address/Service/Group'],
            'subnet': row['Source Address/Member'],
            'description': row['Comment/Description']
        }
        
        
'''
 #For Policies
 
 workbook = pd.read_excel(workbook_path, sheet_name="Firewall Objects")
    
    object_data = {exactly 
        'name': row['Device'],
        'reason': row['Reason'],
        'change_description': row['Change Description'],
        'object_address_service_groupname': row[r"Object'Address/Service/Group' Name"],
        'subnet': row['Source Address/Member'],
        'type': row['Object Type'],
        'description': row['Comment/Description']
    }
'''