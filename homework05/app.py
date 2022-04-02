from flask import Flask, request, jsonify
import redis
import json
from typing import List

app = Flask(__name__)

def get_redis_client():
    '''
    Returns the network over which the Flask and Redis containers communicate
    '''
    return redis.Redis(host='172.17.0.5', port=6379, db=0)

def read_data_from_file() -> List[dict]:
    '''
    Retrieves the meteorite landings data and returns it at a list of dictionaries
    '''
    data = json.load(open('Meteorite_Landings.json', 'r'))
    return data['meteorite_landings']

@app.route('/data', methods=['GET','POST'])
def data():
    '''
    Loads the data into the Redis container if the method requested by the user is POST, or returns the data from 
    the dataset if the method requested is GET
    '''
    rd = get_redis_client()
    if request.method == 'GET':
        data = []
        start = request.args.get('start', 0)
        try:
            start = int(start)
            for key in rd.scan_iter():
                d = rd.hgetall(key)
                d = {key.decode('utf-8'): d[key].decode('utf-8') for key in d.keys()}
                data.append(d)
        except ValueError:
            return ' -- Invalid start parameter. Please ensure the start parameter is an integer --\n'
        return jsonify(data[start:])    
    elif request.method == 'POST':
        data = read_data_from_file()
        for d in data:
            rd.hset(d['id'], mapping=d)
        return ' -- Successfully uploaded data --\n'    
    return ' -- Unknown request --\n'        

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
