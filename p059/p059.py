import itertools as _itertools

def p059(cipher):
	for password in _itertools.product(range(97, 123), repeat=3):
		password = _itertools.cycle(password)
		text = tuple(next(password) ^ ascii_code for ascii_code in cipher)
		if ' the ' in ''.join(map(chr, text)).lower():
			return sum(text)

if __name__ == '__main__':
	print(p059(tuple(map(int, input().split(',')))))