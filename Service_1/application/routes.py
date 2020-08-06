from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import environ
import requests
import random


app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')


db = SQLAlchemy(app)


class superheroes(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    heroname = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return ''.join([
            'Name: ', self.heroname
        ])


@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/heroname')
    print(response)
    sentence = response.text
    post_data = superheroes.query.all()
    db.session.add(superheroes( heroname = sentence ))
    db.session.commit()
    return render_template('index.html', sentence = sentence, title = 'Home', superheroes=post_data)
