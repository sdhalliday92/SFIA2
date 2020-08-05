from application import app
import random


@app.route('/name2', methods=['GET'])
def ending():

	list = ['Machine','Skull','Blaze','King','Storm','Cobra','Thing', 'Dart', 'Boss', 'Speedster', 'God', 'Queen', 'Jester', 'Spaceman', 'Cowboy']
	
	return list[random.randrange(14)]
