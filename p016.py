import sys as _sys

def p016(power):
	return sum(map(int, str(2 ** power)))

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p016(int(_sys.argv[1])))
	else:
		print('Usage: p016 <integer>')
		_sys.exit(1)
