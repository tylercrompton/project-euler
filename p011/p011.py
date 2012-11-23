from functools import reduce as _reduce
from operator import mul as _mul
import sys as _sys

def p011(grid):
	max = 0
	for row in range(len(grid)):
		for cell in range(len(grid[0])):
			if cell <= len(grid[0]) - 4:
				product = _reduce(_mul, grid[row][cell:cell + 4])
				if product > max: max = product
			if row <= len(grid) - 4:
				product = _reduce(_mul, (grid[row + i][cell] for i in range(4)))
				if product > max: max = product
			if cell <= len(grid[0]) - 4 and row <= len(grid) - 4:
				product = _reduce(_mul, (grid[row + i][cell + i] for i in range(4)))
				if product > max: max = product
			if cell > 4 and row <= len(grid) - 4:
				product = _reduce(_mul, (grid[row + i][cell - i] for i in range(4)))
				if product > max: max = product
	return max

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		with open(_sys.argv[1]) as file:
			print(p011([tuple(map(int, line.split())) for line in file]))
	else:
		print('Usage: p011 <file>')
		_sys.exit(1)
