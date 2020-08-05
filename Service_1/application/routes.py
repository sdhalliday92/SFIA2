from application import app
from flask import render_template, request
from os import environ
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
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


class superhero(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name1 = db.Column(db.String(50), nullable=False)
    name2 = db.Column(db.String(50), nullable=False)
   
    def __repr__(self):
        return ''.join(
        [
            'First Name: ' + self.name1 + '\n' 
            'Second Name: ' + self.name2 + '\n'
            'ID: ' + str(self.id)
        ]
    )


@app.route('/', methods=['GET', 'POST'])
def home():
    response = requests.get('http://localhost:5003/generator')
    print(response)
    heroname = response.text
    superhero_data = superhero.query.all()
    return render_template('index.html', heroname=heroname, superhero=superhero_data, title='Home')
