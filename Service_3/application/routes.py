from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def ending():

	list = ['Machine','Skull','Blaze','King','Storm','Cobra','Thing']
	
	return list[random.randrange(6)]
