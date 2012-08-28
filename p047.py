import math as _math
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

def p047(n):
	i = 1
	count = 0
	while count < n:
		if len(set(factor(i))) == n:
			count += 1
		else:
			count = 0
		i += 1
	return i - n

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p047(int(_sys.argv[1])))
	else:
		print('Usage: p047 <integer>')
		_sys.exit(1)
