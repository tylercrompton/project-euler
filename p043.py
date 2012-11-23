from itertools import permutations as _permutations

def p043():
	total = 0
	for permutation in _permutations('0123456789'):
		n = ''.join(permutation)
		if int(n[1:4]) % 2 == 0 and \
				int(n[2:5]) % 3 == 0 and \
				int(n[3:6]) % 5 == 0 and \
				int(n[4:7]) % 7 == 0 and \
				int(n[5:8]) % 11 == 0 and \
				int(n[6:9]) % 13 == 0 and \
				int(n[7:10]) % 17 == 0:
			total += int(n)
	return total

if __name__ == '__main__':
	print(p043())
