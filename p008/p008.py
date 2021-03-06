from functools import reduce as _reduce
from operator import mul as _mul
import sys as _sys

def p008(digits):
	return max(_reduce(_mul, map(int, digits[i:i + 5])) for i in range(len(str(digits)) - 4))

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p008(_sys.argv[1]))
	else:
		print('Usage: p008 <integer>')
		_sys.exit(1)
