import asyncio
import websockets
import json, urllib.request

# import urllib, base64

class NINA_API:
    
    def __init__(self, ip, api_key):
        self.ip = ip
        self.api_key = api_key
        
        
    async def connect(self):
        print("connecting...")
        async with websockets.connect("ws://192.168.137.1:8181/" + "events/v1") as websocket:
            await asyncio.sleep(1)
            await websocket.send(json.dumps({'ApiKey': self.api_key}))
        while True:
            try:
                event = json.loads(await websocket.recv())
                print(event)
                return event
            except websockets.ConnectionClosed:
                break
        asyncio.run(self.connect())
    
    

    
    def status(self, endpoint):
        
        print("Trying to connect...")
        try:
            # with urllib.request.urlopen(self.ip + "/api/v1" + endpoint) as response:
            with urllib.request.urlopen("http://192.168.137.1:8181/api/v1/filterwheel/") as response:
                return json.load(response)
        except:
            return "Error accessing API."

        # request = urllib.request(self.ip + "/api/v1" + endpoint)
        # base64string = base64.b64encode('%s:%s' % ("user", self.api_key))
        # request.add_header("Authorization", "Basic %s" % base64string)   
        # result = urllib.urlopen(request)
        # print(result)





from config import IP as NINA_URL
from config import API_KEY as NINA_KEY


nina = NINA_API(NINA_URL, NINA_KEY)

print(nina.api_key)
print(nina.ip)

asyncio.run(nina.connect())

  