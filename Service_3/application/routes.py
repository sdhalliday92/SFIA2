from application import app
import random


@app.route('/name2', methods=['GET'])
def ending():

	list = ['Machine','Skull','Blaze','King','Storm','Cobra','Thing', 'Dart', 'Blue', 'Red']
	
	return list[random.randrange(9)]
