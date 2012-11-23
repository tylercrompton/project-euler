import math as _math
import sys as _sys

def p039(p):
	max = (-1, -1)
	for p in range(3, p + 1):
		count = 0
		for a in range(1, p + 1):
			for b in range(a + 1, p - a):
				c = _math.sqrt(a ** 2 + b ** 2)
				if a + b + c == p:
					count += 1
		if count > max[1]:
			max = (p, count)
	return max[0]

if __name__ == '__main__':
	print(p039(int(_sys.argv[1])))
