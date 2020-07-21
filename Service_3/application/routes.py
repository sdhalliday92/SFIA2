from application import app
import random


@app.route('/randomname', methods=['GET'])
def ending():

	list = ['Machine','Skull','Blaze','King','Storm','Cobra','Thing']
	
	return list[random.randrange(6)]
