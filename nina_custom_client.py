import asyncio
import websockets
import json, urllib.request

class NINA_API:
    
    def __init__(self, ip, api_key):
        self.ip = ip
        self.api_key = api_key
        
        
    async def connect(self):
        async with websockets.connect(self.ip + "events/v1") as websocket:
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
        try:
            with urllib.request.urlopen(self.ip + endpoint) as response:
                return json.load(response)
        except:
            return "Error accessing API."
    
    
  