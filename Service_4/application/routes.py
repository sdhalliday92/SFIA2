from application import app
import requests


@app.route('/superhero', methods=['GET'])
def sentence():
    beginning = requests.get('http://localhost:5001/name1')
    ending = requests.get('http://localhost:5002/name2')
    response = beginning.text + " " + ending.text
    return response
