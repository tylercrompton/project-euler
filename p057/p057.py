from fractions import Fraction as _Fraction

def memoize(function):
	memos = {}
	def wrapper(*args):
		try:
			return memos[args]
		except KeyError:
			memos[args] = function(*args)
			return memos[args]
	return wrapper

@memoize
def fraction_expansion(n):
	if n == 0:
		return _Fraction(1, 1)
	if n == 1:
		return _Fraction(3, 2)
	previous_fraction = fraction_expansion(n - 1)
	return _Fraction(2 * previous_fraction.numerator + fraction_expansion(n - 2).numerator, previous_fraction.numerator + previous_fraction.denominator)

def p057():
	count = 0
	for n in range(1, 1001):
		fraction = fraction_expansion(n)
		if len(str(fraction.numerator)) > len(str(fraction.denominator)):
			count += 1
	return count

if __name__ == '__main__':
	print(p057())