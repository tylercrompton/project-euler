import sys as _sys

def p006(lower_bound, upper_bound):
	return sum(range(lower_bound, upper_bound + 1)) ** 2 - sum(map(lambda x: x ** 2, range(lower_bound, upper_bound + 1)))

if __name__ == '__main__':
	if len(_sys.argv) == 3:
		print(p006(int(_sys.argv[1]), int(_sys.argv[2])))
	else:
		print('Usage: p006 <integer> <integer>')
		_sys.exit(1)
