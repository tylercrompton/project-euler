from math import factorial as _factorial
import sys as _sys

def p020(number):
	return sum(map(int, str(_factorial(number))))

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p020(int(_sys.argv[1])))
	else:
		print('Usage: p020 <integer>')
		_sys.exit(1)
