def p052():
	i = 1
	while True:
		if sorted(str(i)) == sorted(str(2 * i)) == sorted(str(3 * i)) == sorted(str(4 * i)) == sorted(str(5 * i)) == sorted(str(6 * i)):
			return i
		i += 1

if __name__ == '__main__':
	print(p052())
