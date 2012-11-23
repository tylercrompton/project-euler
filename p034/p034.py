from functools import reduce as _reduce

def digitize(n):
	while n != 0:
		yield n % 10
		n //= 10

def undigitize(digits):
	i = len(digits) - 1
	n = 0
	while i >= 0:
		n += digits[len(digits) - i - 1] * 10 ** i
		i -= 1
	return n

def factorial(n):
	if n in (0, 1): return 1
	return n * factorial(n - 1)

def p034():
	for n in range(10, 100000):
		if sum(map(factorial, digitize(n))) == n:
			yield n

if __name__ == '__main__':
	print(sum(p034()))
