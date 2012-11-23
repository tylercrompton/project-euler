def is_triangular(n):
	i = 1
	t = 1
	while t <= n:
		if n == t:
			return True
		i += 1
		t = i / 2 * (i + 1)
	return False

def p042(words):
	total = 0
	for word in words:
		if is_triangular(sum(map(lambda char: ord(char) - 64, word))):
			total += 1
	return total

if __name__ == '__main__':
	words = input().split('","')
	words[0] = words[0][1:]
	words[-1] = words[-1][:-1]
	print(p042(words))
