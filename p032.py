from itertools import permutations as _permutations

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

def p032():
	for a in range(92):
		digitized_a = tuple(digitize(a))
		if a % 11 == 0 or a % 10 == 0:
			continue
		remaining_digits = set(range(1, 10)).difference(digitize(a))
		for i in range(2, 5):
			for permutation in _permutations(sorted(remaining_digits), i):
				b = undigitize(permutation)
				c = a * b
				if c > 98765:
					break
				digitized_c = tuple(digitize(c))
				if 0 in digitized_c:
					continue
				if sorted(digitized_a + tuple(digitize(b)) + digitized_c) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
					yield c
		
if __name__ == '__main__':
	print(sum(set(p032())))
