def repeating_decimals(n):
	remainders = [1]
	while True:
		remainder = remainders[-1] * 10 % n
		for i in range(len(remainders) - 1, -1, -1):
			if remainder == remainders[i]:
				return len(remainders) - i
		remainders.append(remainder)

if __name__ == '__main__':
	print(max(range(2, 1000), key=repeating_decimals))
