from collections import Counter as _Counter
from functools import reduce as _reduce
import math as _math
from operator import mul as _mul
import sys as _sys

def factor(number):
	factors = [1]
	factored = False
	while not factored:
		for i in range(2, _math.floor(_math.sqrt(number)) + 1):
			if number % i == 0:
				number //= i
				factors.append(i)
				break
		else:
			factors.append(number)
			factored = True
	return factors

def p005(lower_bound, upper_bound):
	factors = _Counter()
	for i in range(lower_bound, upper_bound + 1):
		for multiple, count in _Counter(factor(i)).items():
			if count > factors.get(multiple, 0):
				factors[multiple] = count
	return _reduce(_mul, (k ** v for k, v in factors.items()))

if __name__ == '__main__':
	if len(_sys.argv) == 3:
		print(p005(int(_sys.argv[1]), int(_sys.argv[2])))
	else:
		print('Usage: p005 <integer> <integer>')
		_sys.exit(1)
