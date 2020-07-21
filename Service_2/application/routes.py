from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def beginning():

	list = ['Captain','Super','Phantom','Omega','Shadow','Silver','Doctor']
	
	return list[random.randrange(6)]
