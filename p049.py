from itertools import permutations as _permutations
import sys as _sys

def primes(ceiling):
	'''Calculate the prime numbers.'''
	numbers = [False] * ceiling
	numbers[0] = numbers[1] = True
	step = 2
	while step < ceiling:
		if numbers[step]:
			step += 1
		else:
			yield step
			i = step
			while i < ceiling:
				numbers[i] = True
				i += step

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

def p037():
	primes_ = set(primes(10000))
	for a in primes_:
		permutations = tuple(set(map(undigitize, set(_permutations(digitize(a))))).intersection(primes_))
		for i in range(1, len(permutations)):
			b = permutations[i]
			for j in range(i + 1, len(permutations)):
				c = permutations[j]
				if a != 1487 and b in primes_ and c in primes_ and (a + c) // 2 == b:
					return str(a) + str(b) + str(c)

if __name__ == '__main__':
	print(p037())
