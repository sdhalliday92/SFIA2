from application import app
import requests


@app.route('/superhero', methods=['GET'])
def sentence():
    beginning = requests.get('http://service_2:5001/name1')
    ending = requests.get('http://service_3:5002/name2')
    response = beginning.text + " " + ending.text
    return response
