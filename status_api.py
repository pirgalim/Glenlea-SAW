from flask import Flask, jsonify
import json, urllib.request


PWI_URL = 'http://localhost:8220/status'
PORT = 5005


app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():    
    try:
        with urllib.request.urlopen(PWI_URL) as response:
            return json.load(response)
    except:
        return jsonify('An error has occurred')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=PORT)