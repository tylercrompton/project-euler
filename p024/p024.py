from itertools import permutations as _permutations
import sys as _sys

def p024():
	return ''.join(tuple(_permutations('0123456789'))[999999])

if __name__ == '__main__':
	if len(_sys.argv) == 1:
		print(p024())
	else:
		print('Usage: p024')
		_sys.exit(1)
