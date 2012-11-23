import sys as _sys

def p013(numbers):
	return str(sum(numbers))[:10]

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		with open(_sys.argv[1]) as file:
			print(p013(map(int, file)))
	else:
		print('Usage: p013 <file>')
		_sys.exit(1)
