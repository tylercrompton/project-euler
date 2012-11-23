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

def p035(ceiling):
	primes_ = set(primes(undigitize(max((tuple(digitize(n)) for n in range(ceiling)), key=sorted))))
	circular_primes = []
	for prime in primes_:
		if prime >= ceiling:
			continue
		digits = tuple(digitize(prime))
		if all(undigitize(digits[i:] + digits[0:i]) in primes_
				for i in range(len(digits))):
			circular_primes.append(prime)
	return len(circular_primes)

if __name__ == '__main__':
	print(p035(int(_sys.argv[1])))
