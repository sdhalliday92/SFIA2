from application import app
import requests


@app.route('/randomhero', methods=['GET'])
def sentence():
    beginning = requests.get('http://service_2:5001/randomname')
    ending = requests.get('http://service_3:5002/randomname')
    response = beginning.text + " " + ending.text
    return response
