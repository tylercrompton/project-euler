import math as _math
import sys as _sys

def p4(digit_count):
	temp = str(int('9' * digit_count) ** 2)
	temp = str(int(temp[:len(temp) // 2]) - 1)
	number = int(temp + ''.join(reversed(temp)))

	max_divisor = int('9' * digit_count)
	minimum = 10 ** (digit_count - 1) ** 2
	while number > minimum:
		if number == int(''.join(reversed(str(number)))):
			divisor = _math.ceil(_math.sqrt(number))
			while divisor <= max_divisor:
				if number % divisor == 0:
					return number
				divisor += 1
		number -= 1

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p4(int(_sys.argv[1])))
	else:
		print('Usage: p4 <integer>')
		_sys.exit(1)
