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
def factorial(n):
	if n in (0, 1):
		return 1
	return n * factorial(n - 1)

def combinatorics(n, r):
	return factorial(n) / (factorial(r) * factorial(n - r))

def p053():
	count = 0
	for n in range(1, 101):
		for r in range(1, n + 1):
			if combinatorics(n, r) > 1000000:
				count += 1
	return count

if __name__ == '__main__':
	print(p053())
