from application import app
import random


@app.route('/randomname', methods=['GET'])
def beginning():

	list = ['Captain','Super','Phantom','Omega','Shadow','Silver','Doctor']
	
	return list[random.randrange(6)]
