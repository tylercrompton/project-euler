def memoize(function):
	memos = {}
	def wrapper(*args):
		try:
			return memos[args]
		except KeyError:
			memos[args] = function(*args)
			return memos[args]
		except TypeError:
			return function(*args)
	return wrapper

@memoize
def p031(target_pence, largest_coin=200):
	if target_pence < 0:
		return 0
	elif target_pence == 0:
		return 1

	return sum(p031(target_pence - coin, coin) for coin in tuple(filter(lambda coin: coin <= largest_coin, (1, 2, 5, 10, 20, 50, 100, 200))))

if __name__ == '__main__':
	print(p031(200))
