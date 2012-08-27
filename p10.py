from itertools import repeat as _repeat
from math import ceil as _ceil
import sys as _sys

def p10(ceiling):
	numbers = list(range(2, ceiling))
	i = 0
	while i < ceiling - 2:
		jump = numbers[i]
		numbers[i + jump:ceiling - 2:jump] = _repeat(0, _ceil((len(numbers) - i) / jump) - 1)
		i += 1
		while i < ceiling - 2 and numbers[i] == 0:
			i += 1
	return sum(numbers)

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p10(int(_sys.argv[1])))
	else:
		print('Usage: p10 <integer>')
		_sys.exit(1)
