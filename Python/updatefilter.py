import requests


sms_server = '0.0.0.0'
parameters = {
    ""
}

def update_filter_api():
    url = f"https://" + sms_server + "/ipsProfileMgmt/setFilters?" + parameters
    response = requests.post(url)



https://docs.trendmicro.com/all/tip/sms/v5.2.0/en-us/sms_5.2.0_web_api_guide.pdf
https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/
https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/