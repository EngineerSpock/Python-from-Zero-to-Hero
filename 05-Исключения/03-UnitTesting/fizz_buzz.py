def get_reply(number):
	if number%5==0 and number%3==0:
		return 'FizzBuzz'
	elif number%3==0:
		return 'Fizz'
	elif number%5==0:
		return 'Buzz'
	else:
		return ''