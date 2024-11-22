from flask import Flask, jsonify
from pwi4_client import PWI4


PORT = 5005


app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():    
    try:
        
        print("Connecting to PWI4...")

        pwi4 = PWI4()
        s = pwi4.status()
        
        message = "Mount connected:", s.mount.is_connected
        print(message)
            
        return jsonify(message)
        
    except:
        return jsonify('An error has occurred')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=PORT)