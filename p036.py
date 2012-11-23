import sys as _sys

def p036(ceiling):
	total = 0
	for n in range(ceiling):
		if bin(n)[2:] == ''.join(reversed(bin(n)[2:])) and str(n) == ''.join(reversed(str(n))):
			total += n
	return total

if __name__ == '__main__':
	print(p036(int(_sys.argv[1])))
