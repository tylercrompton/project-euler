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
	primes_ = set(primes(1000000))
	answer = []

	for prime in primes_:
		digits = tuple(digitize(prime))
		if all(undigitize(digits[i:]) in primes_ and undigitize(digits[:-i]) in primes_ for i in range(1, len(digits))):
			answer.append(prime)
	return sum(answer) - 2 - 3 - 5 - 7
if __name__ == '__main__':
	print(p037())
