from collections import Counter as _Counter
import functools as _functools
from itertools import combinations as _combinations
import math as _math
from operator import mul as _mul

def memoize(function):
	memos = {}
	def wrapper(*args):
		try:
			return memos[args]
		except KeyError:
			memos[args] = function(*args)
			return memos[args]
		except TypeError:
			return function(*args)

	_functools.update_wrapper(wrapper, function)
	return wrapper

@memoize
def prime_factors(number):
	i = 2
	square_root = _math.floor(_math.sqrt(number))
	while i <= square_root:
		if number % i == 0:
			return (i,) + prime_factors(number // i)
		i += 1
	return (number,)

@memoize
def factors(number):
	'''Find all positive factors of a positive integer.'''

	_prime_factors = prime_factors(number)
	combinations = set()
	for i in range(1, len(_prime_factors) + 1):
		combinations.update(_combinations(_prime_factors, i))
	return {_functools.reduce(_mul, combination) for combination in combinations}.union({1})

if __name__ == '__main__':
	amicable_numbers = set()
	for i in range(2, 10000):
		_ = sum(factors(i)) - i
		if i != _ and i == sum(factors(_)) - _:
			amicable_numbers.add(i)
	print(sum(amicable_numbers))
