from operator import itemgetter as _itemgetter

def gcf(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b, *args):
	lcm_ = a * b // gcf(a, b)
	if len(args):
		return lcm(lcm_, *args)
	print(lcm_)
	return lcm_

def p033():
	numerator = 1
	denominator = 1
	for n in range(1, 9):
		for d in range(n + 1, 10):
			for i in set(range(1, 10)).difference((n, d)):
				if (10 * n + i) / (10 * i + d) == n / d:
					numerator *= 10 * n + i
					denominator *= 10 * i + d
	return numerator, denominator

if __name__ == '__main__':
	answer = p033()
	gcf_ = gcf(answer[0], answer[1])
	print(answer[1] // gcf_)
