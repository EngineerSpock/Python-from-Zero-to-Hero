import unittest
import fizz_buzz

class FizzBuzzTests(unittest.TestCase):

	def test_fizz(self):
		number=6
		
		result = fizz_buzz.get_reply(number)
		
		self.assertEqual(result, 'Fizz')
		
	def test_buzz(self):
		number=10
		
		result = fizz_buzz.get_reply(number)
		
		self.assertEqual(result, 'Buzz')
		
	def test_fizzbuzz(self):
		number=15
		result = fizz_buzz.get_reply(number)
		
		self.assertEqual(result, 'FizzBuzz')
		
if __name__ == '__main__':
	unittest.main()