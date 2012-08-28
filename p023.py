from functools import reduce as _reduce
from itertools import combinations as _combinations
import math as _math
from operator import mul as _mul
import sys as _sys

def factor(number):
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

def divisors(number):
    factors = tuple(factor(number))
    combinations = set()
    for i in range(1, len(tuple(factors)) + 1):
        combinations.update(_combinations(factors, i))
    return [1] + sorted(_reduce(_mul, combination) for combination in combinations)

def p023():
	abundant_numbers = []
	for i in range(12, 28112):
		if sum(divisors(i)[:-1]) > i:
			abundant_numbers.append(i)
	inverse = set()
	for i in range(len(abundant_numbers)):
		for j in range(i, len(abundant_numbers)):
			total = abundant_numbers[i] + abundant_numbers[j]
			if total <= 28123: inverse.add(total)
			else: break
	return sum(set(range(1, 28124)).difference(inverse))

if __name__ == '__main__':
	if len(_sys.argv) == 1:
		print(p023())
	else:
		print('Usage: p023')
		_sys.exit(1)
