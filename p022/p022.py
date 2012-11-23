from csv import reader as _reader
from string import ascii_uppercase as _ascii_uppercase
import sys as _sys

def p022(words):
	words.sort()
	return sum((i + 1) * sum(_ascii_uppercase.find(char) + 1 for char in words[i]) for i in range(len(words)))

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		with open(_sys.argv[1], newline='') as file:
			print(p022(next(_reader(file))))
	else:
		print('Usage: p022 <file>')
		_sys.exit(1)
