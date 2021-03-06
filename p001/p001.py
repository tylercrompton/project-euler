import sys as _sys

def p001(max):
	i = 0
	total = 0

	while i < max:
		if i + 15 < max:
			total += i * 7 + 60
		elif i + 12 < max:
			total += i * 6 + 45
		elif i + 10 < max:
			total += i * 5 + 33
		elif i + 9 < max:
			total += i * 4 + 23
		elif i + 6 < max:
			total += i * 3 + 14
		elif i + 5 < max:
			total += i * 2 + 8
		elif i + 3 < max:
			return total + i + 3
		i += 15

	return total

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p001(int(_sys.argv[1])))
	else:
		print('Usage: p001 <integer>')
		_sys.exit(1)
