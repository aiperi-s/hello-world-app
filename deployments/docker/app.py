from flask import Flask,  jsonify 
import os 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'Hello I am a developer my name is Aiperi S',
        'environment': os.environ.get('ENVIRONMENT'),
        'owner': 'aiperi-s'
        'namespace': os.environ.get('NAMESPACE')
    })
    
@app.route('/aiperi-s')
def comming_soon():
    return jsonify({
        'message': 'This is my page'
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)