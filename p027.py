import math as _math

def is_prime(n):
	i = 2
	sqrt = _math.floor(_math.sqrt(abs(n)))
	while i < sqrt:
		if n % i == 0:
			return False
		i += 1
	return True

def f(a, b, n):
	return n ** 2 + a * n + b

def p027():
	max = (-1, -1, -1)
	for a in range(-999, 1000):
		for b in range(-999, 1000):
			n = 0
			while is_prime(f(a, b, n)):
				n += 1
			if n > max[2]:
				max = (a, b, n)
	return max[0] * max[1]

if __name__ == '__main__':
	print(p027())
