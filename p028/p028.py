import sys as _sys

def p028(size):
	return sum(4 * size ** 2 - 6 * size + 6 for size in range(size, 1, -2)) + 1

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p028(int(_sys.argv[1])))
	else:
		print('Usage: p028 <odd integer>')
		_sys.exit(1)
