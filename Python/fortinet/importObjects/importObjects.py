import pandas as pd
import requests

#if located within another directory. COMMENT OUT IF IN THE SAME DIRECTORY.
workbook_path = r'C:\Users\devih\Documents\Git\Automation\Python\fortinet\file.xlsx'

#Enter the workbook variable or file name
workbook = pd.read_excel(workbook_path)
'''
#Prepare data and headers for Fortinet API
fortinet_api_url = 'https://your-fortinet-api-url.com'
api_endpoint = '/api/v1/data'
api_url = f'{fortinet_api_url}{api_endpoint}'

# Assuming you have an API key for authentication
api_key = 'your_api_key'
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
'''

# Iterate through each row in the DataFrame
for index, row in workbook.iterrows():
    # Extract policy information from the current row
    policy_data = {
        'from_host': row['From Host'],
        'from_ip': row['IP Address'],
        'to': row['To'],
        'to_host': row['Host'],
        'to_ip': row['IP Address'],
        'port': row['Port'],
        'description': row['Description']
    }

    print(policy_data)

'''
    # Prepare payload for policies
    policy_payload = {'data': policy_data}

    # Send data for policies to Fortinet API
    try:
        response_policy = requests.post(api_url, json=policy_payload, headers=headers)

        if response_policy.status_code // 100 == 2:
            print(f'Policy data for row {index} successfully pushed to Fortinet.')
        else:
            print(f'Failed to push policy data for row {index}. Status code: {response_policy.status_code}, Response: {response_policy.text}')

    except requests.RequestException as e:
        print(f'Error pushing policy data for row {index}: {e}')
'''