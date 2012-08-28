import sys as _sys

def spell_number(number):
	ones = {
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine'
	}
	teens = {
		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		14: 'fourteen',
		15: 'fifteen',
		16: 'sixteen',
		17: 'seventeen',
		18: 'eighteen',
		19: 'nineteen'
	}
	tens = {
		1: 'ten',
		2: 'twenty',
		3: 'thirty',
		4: 'forty',
		5: 'fifty',
		6: 'sixty',
		7: 'seventy',
		8: 'eighty',
		9: 'ninety'
	}

	spelling = ''
	if len(str(number)) == 4:
		spelling += ones[int(str(number)[0])] + 'thousand'
		number %= 1000
	if len(str(number)) == 3:
		spelling += ones[int(str(number)[0])] + 'hundred'
		number %= 100
		if number > 0:
			spelling += 'and'
	if len(str(number)) == 2:
		if number >= 20:
			spelling += tens[int(str(number)[0])]
			number %= 10
		else:
			spelling += teens[number]
			number = 0
	if len(str(number)) == 1:
		try:
			spelling += ones[number]
		except KeyError:
			pass
	return spelling

def p017(lower_bound, upper_bound):
	return sum(len(spell_number(number)) for number in range(lower_bound, upper_bound + 1))

if __name__ == '__main__':
	if len(_sys.argv) == 3:
		print(p017(int(_sys.argv[1]), int(_sys.argv[2])))
	else:
		print('Usage: p017 <integer> <integer>')
		_sys.exit(1)
