from flask import Flask, jsonify
from pwi4_client import PWI4


PORT = 5005


app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():    
    try:
        
        status = dict()
        
        print("Connecting to PWI4...")

        pwi4 = PWI4()
        s = pwi4.status()
        
        # connect = "Mount connected:", s.mount.is_connected
        
        
        # status['mount'] = s.mount.is_connected
        
        # status['time'] = s.response.timestamp
        

        status = s.raw
            
        return jsonify(status)
        
    except:
        return jsonify('An error has occurred')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=PORT)