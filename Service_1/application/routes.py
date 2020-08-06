from application import app
from flask import render_template, request
import requests
import random


class Superheroes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(100), nullable=False)
    name2 = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return ''.join([
            'User ID: ', self.user_id, '\r\n',
            'Name: ', self.name1, '\r\n', self.name2
        ])


@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/heroname')
    print(response)
    sentence = response.text
    post_data = Superheroes.query.all()
    return render_template('index.html', sentence = sentence, title = 'Home', superheroes=post_data)
