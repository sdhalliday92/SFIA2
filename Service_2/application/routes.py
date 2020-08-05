from application import app
import random


@app.route('/name1', methods=['GET'])
def beginning():

	list = ['Captain','Super','Phantom','Omega','Shadow','Silver','Doctor', 'Incredible', 'Amazing', 'Big', 'Gold', 'Flying', 'Aqua', 'Speed', 'Stretch']
	
	return list[random.randrange(14)]
