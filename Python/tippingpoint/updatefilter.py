import requests

sms_server = '0.0.0.0'

filter_id = ()

filter_disabled_param = {
        "profile": "Basic",
        "name": "JSON FILE", 
        "comment": "dking7 Tipping Point Update",
        "enabled": False
}

filter_block_param = {
        "profile": "Basic",
        "name": "JSON FILE", 
        "comment": " dking7 Tipping Point Update",
        "actionset": "Block+Notify"
}

class modify_filter():
    def __init__(self, server, disabled_params, block_params):
        filter_disabled_param = {
            "comment": " dking7 Tipping Point Update",
            "enabled": False
}

        filter_block_param = {
            "comment": " dking7 Tipping Point Update"      
}
        
        self.server = server
        self.disabled_params = disabled_params
        self.block_params = block_params
    
    def block_filter_api(self):
        url = f"https://" + self.server + "/ipsProfileMgmt/setFilters?" + filter_block_param
        requests.post(url)
    
    def disabled_filter_api(self):
        url = f"https://" + sms_server + "/ipsProfileMgmt/setFilters?" + filter_disabled_param
        requests.post(url)


filter = modify_filter.disabled_filter_api("10.235.217.109",
    
    
    
    
    )












https://docs.trendmicro.com/all/tip/sms/v5.2.0/en-us/sms_5.2.0_web_api_guide.pdf
https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/
https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/