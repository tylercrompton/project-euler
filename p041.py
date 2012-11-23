from itertools import permutations as _permutations
import math as _math
import sys as _sys

def digitize(n):
	digits = []
	while n != 0:
		digits.append(n % 10)
		n //= 10
	return reversed(digits)

def undigitize(digits):
	i = len(digits) - 1
	n = 0
	while i >= 0:
		n += digits[len(digits) - i - 1] * 10 ** i
		i -= 1
	return n

def is_prime(n):
	i = 2
	while i < _math.floor(_math.sqrt(n)):
		if n % i == 0:
			return False
		i += 1
	return True

def p041():
	for i in range(9, 0, -1):
		for permutation in _permutations(range(i, 0, -1)):
			if is_prime(undigitize(permutation)):
				return undigitize(permutation)

if __name__ == '__main__':
	print(p041())
