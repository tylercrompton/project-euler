def p030(digits):
	return sum({i for i in range(2, 10 ** (digits + 1)) if sum(map(lambda d: int(d) ** digits, str(i))) == i})

if __name__ == '__main__':
	print(p030(5))