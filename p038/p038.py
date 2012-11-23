from itertools import permutations as _permutations
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

def p038():
	i = 1
	max = -1
	while True:
		t = ''
		n = 0
		while len(t) < 9:
			n += 1
			t += str(i * n)
		if n == 2 and len(t) > 9:
			break
		if sorted(t) == ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and int(t) > max:
			max = int(t)
		i += 1
	return max

if __name__ == '__main__':
	print(p038())
