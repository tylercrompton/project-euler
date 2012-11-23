import math as _math
import sys as _sys

def p003(number):
	if number == 0: return float('inf')

	factored = False
	while True:
		for i in range(2, _math.floor(_math.sqrt(abs(number))) + 1):
			if number % i == 0:
				number /= i
				break
		else:
			return int(number)

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p003(int(_sys.argv[1])))
	else:
		print('Usage: p003 <integer>')
		_sys.exit(1)
