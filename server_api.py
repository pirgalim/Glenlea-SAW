from flask import Flask
from flask_cors import CORS
import json, urllib.request

app = Flask(__name__)
CORS(app)

LOCAL_IP = 'http://10.84.3.29:5005/status'
PORT = 16001

@app.route("/", methods=["GET"])
def status():
    try:
        with urllib.request.urlopen(LOCAL_IP) as response:
            return json.load(response)
    except:
        return "Error accessing API."
        
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=PORT)