import math as _math
import sys as _sys

def p009(total):
	for a in range(3, total // 3):
		b = a + 1
		c = _math.sqrt(a ** 2 + b ** 2)
		while a + b + c <= total:
			if c == _math.floor(c):
				c = _math.floor(c)
				if a + b + c == total:
					return a * b * c
			b += 1
			c = _math.sqrt(a ** 2 + b ** 2)

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p009(int(_sys.argv[1])))
	else:
		print('Usage: p009 <integer>')
		_sys.exit(1)
