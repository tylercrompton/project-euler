import sys as _sys

def length_of_collatz_sequence(number):
	try:
		length_of_collatz_sequence._memos
	except AttributeError:
		length_of_collatz_sequence._memos = {1: 1}

	delta = 0
	sequence = []
	n = number
	while True:
		try:
			delta = length_of_collatz_sequence._memos[n]
			break
		except KeyError:
			pass

		sequence.append(n)
		if n % 2 == 0:
			n //= 2
		else:
			n = 3 * n + 1

	for length, key in enumerate(reversed(sequence)):
		length_of_collatz_sequence._memos[key] = length + 1 + delta

	return length_of_collatz_sequence._memos[number]

def p014(lower_bound, upper_bound):
	return max((length_of_collatz_sequence(i), i) for i in range(lower_bound, upper_bound + 1))[1]

if __name__ == '__main__':
	if len(_sys.argv) == 3:
		print(p014(int(_sys.argv[1]), int(_sys.argv[2])))
	else:
		print('Usage: p014 <integer> <integer>')
		_sys.exit(1)
