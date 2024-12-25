import json, urllib.request

class NINA_API:
    
    def __init__(self, ip, api_key):
        self.ip = ip
        self.api_key = api_key
        
        
    def connect(self):
        pass
    

    
    def status(self, endpoint):
        try:
            with urllib.request.urlopen(self.ip + endpoint) as response:
                return json.load(response)
        except:
            return "Error accessing API."
    
    
  