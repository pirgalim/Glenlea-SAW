from flask import Flask, jsonify
from flask_cors import CORS
from pwi4_client import PWI4

PORT = 5005

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
    
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=PORT)