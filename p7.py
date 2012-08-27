import sys as _sys

def primes():
	primes = []
	i = 2
	while True:
		if not any(i % prime == 0 for prime in primes):
			yield i
			primes.append(i)
		i += 1

def p6(n):
	prime_generator = primes()
	for i in range(n - 1):
		next(prime_generator)
	return next(prime_generator)

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p6(int(_sys.argv[1])))
	else:
		print('Usage: p7 <integer>')
		_sys.exit(1)
