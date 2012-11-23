def digitize(n):
	digits = []
	while n != 0:
		digits.append(n % 10)
		n //= 10
	return reversed(digits)

def p056():
	return max(sum(digitize(a ** b)) for a in range(1, 100) for b in range(1, 100))

if __name__ == '__main__':
	print(p056())