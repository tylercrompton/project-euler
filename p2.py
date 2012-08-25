import sys as _sys

def p2(upper_bound):
	if upper_bound <= 2: return 0

	buffer = [0, 2]

	sum = 2
	temp = 8
	while temp < upper_bound:
		buffer[0], buffer[1] = buffer[1], temp
		sum += temp
		temp = 4 * buffer[1] + buffer[0]

	return sum

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p2(int(_sys.argv[1])))
	else:
		print('Usage: p2 <integer>')
		_sys.exit(1)
