from flask import Flask, jsonify
from flask_cors import CORS
from pwi4_client import PWI4

from nina_custom_client import NINA_API

PORT = 5005


#TODO: replace this process with a config file
# Startup settings for exe file
NINA_URL = input("Enter the NINA IP: ")
NINA_KEY = input("Enter the NINA API key: ")
print(NINA_KEY)



app = Flask(__name__)
CORS(app)

@app.route('/status', methods=['GET'])
def status():    
    try:
        print("Connecting to PWI4...")
        pwi4 = PWI4()
        s = pwi4.status()            
        return jsonify(s.raw)    
    except:
        return jsonify('Unable to connect to PWI4...')
    
    
    
@app.route('/nina/check', methods=['GET'])
def check():
    nina = NINA_API(NINA_URL, NINA_KEY)
    nina.status("/dome")
    nina.status("/filterwheel")
    nina.status("/focuser")
    
    
@app.route('/nina/listener', methods=['GET'])
def event_listener():
    nina = NINA_API(NINA_URL, NINA_KEY)
    nina.connect()
    
    
    
    

    
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=PORT)
   