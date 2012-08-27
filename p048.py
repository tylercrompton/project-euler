import sys as _sys

def p048(lower_bound, upper_bound):
	return str(sum(i**i for i in range(lower_bound, upper_bound + 1)))[-10:]

if __name__ == '__main__':
	if len(_sys.argv) == 3:
		print(p048(int(_sys.argv[1]), int(_sys.argv[2])))
	else:
		print('Usage: p048 <integer> <integer>')
		_sys.exit(1)
