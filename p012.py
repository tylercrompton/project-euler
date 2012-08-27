from itertools import combinations as _combinations
import math as _math
import sys as _sys

def prime_factor(number):
    factors = [1]
    factored = False
    while not factored:
        for i in range(2, _math.floor(_math.sqrt(number)) + 1):
            if number % i == 0:
                yield i
                number //= i
                break
        else:
            yield number
            factored = True

def p012(min_divisors):
	i = 1
	jump = 2
	while True:
		prime_factors = tuple(prime_factor(i))
		number_of_factors = sum(len(set(_combinations(prime_factors, i))) for i in range(1, len(prime_factors) + 1)) + 1
		if number_of_factors > min_divisors:
			return i
		i += jump
		jump += 1

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p012(int(_sys.argv[1])))
	else:
		print('Usage: p012 <integer>')
		_sys.exit(1)
