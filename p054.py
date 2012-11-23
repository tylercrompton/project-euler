from collections import Counter as _Counter
from itertools import chain as _chain
from operator import attrgetter as _attrgetter, itemgetter as _itemgetter
import sys as _sys

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

def get_score(cards):
	main = None
	values = list(get_values(cards))
	while 1 in values:
		values.remove(1)
		values.append(14)
	if is_royal_flush(cards):
		main = 9
		values = [14, 13, 12, 11, 10]
	elif is_straight_flush(cards):
		main = 8
		if 1 in cards and 2 in cards:
			values.remove(14)
			values.append(1)
		values = sorted(values, reverse=True)
	elif is_four_of_a_kind(cards):
		main = 7
		values = list(_chain.from_iterable(map(lambda item: [item[0]] * item[1], sorted(_Counter(values).items(), key=_itemgetter(1), reverse=True))))
	elif is_full_house(cards):
		main = 6
		values = list(_chain.from_iterable(map(lambda item: [item[0]] * item[1], sorted(_Counter(values).items(), key=_itemgetter(1), reverse=True))))
	elif is_flush(cards):
		main = 5
		values = sorted(values, reverse=True)
	elif is_straight(cards):
		main = 4
		if 1 in cards and 2 in cards:
			values.remove(14)
			values.append(1)
		values = sorted(values, reverse=True)
	elif is_three_of_a_kind(cards):
		main = 3
		values = list(_chain.from_iterable(map(lambda item: [item[0]] * item[1], sorted(_Counter(values).items(), key=_itemgetter(1), reverse=True))))
		if values[3] < values[4]:
			values[3], values[4] = values[4], values[3]
	elif is_two_pair(cards):
		main = 2
		values = list(_chain.from_iterable(map(lambda item: [item[0]] * item[1], sorted(_Counter(values).items(), key=_itemgetter(1), reverse=True))))
		if values[0] < values[2]:
			values[0:2], values[2:4] = values[2:4], values[0:2]
	elif is_one_pair(cards):
		main = 1
		values = list(_chain.from_iterable(map(lambda item: [item[0]] * item[1], sorted(_Counter(values).items(), key=_itemgetter(1), reverse=True))))
		high = max(tuple(enumerate(values))[2:], key=_itemgetter(1))[0]
		values[2], values[high] = values[high], values[2]
		if values[3] < values[4]:
			values[3], values[4] = values[4], values[3]
	else:
		main = 0
		values = sorted(values, reverse=True)
	return [main] + values

def get_values(cards):
	return tuple(map(_attrgetter('value'), cards))

def is_one_pair(cards):
	values = _Counter(get_values(cards)).values()
	return 2 in values and len(values) == 4

def is_two_pair(cards):
	return _Counter(_Counter(get_values(cards)).values()).get(2, 0) == 2

def is_three_of_a_kind(cards):
	return 3 in _Counter(get_values(cards)).values()

def is_straight(cards):
	values = list(get_values(cards))
	if 1 in values and 13 in values:
		values.remove(1)
		values.append(14)
	lowest = min(values)
	return [value - lowest for value in sorted(values)] == [0, 1, 2, 3, 4]

def is_flush(cards):
	return len(set(map(_attrgetter('suit'), cards))) == 1

def is_full_house(cards):
	values = _Counter(get_values(cards)).values()
	return 2 in values and 3 in values

def is_four_of_a_kind(cards):
	return 4 in _Counter(get_values(cards)).values()

def is_straight_flush(cards):
	return is_straight(cards) and is_flush(cards)

def is_royal_flush(cards):
	return sorted(get_values(cards)) == [1, 10, 11, 12, 13] and is_flush(cards)

def p054(player1, player2):
	return get_score(player1) > get_score(player2)

if __name__ == '__main__':
	values = 'A23456789TJQK'
	count = 0
	for line in _sys.stdin.readlines():
		cards = []
		for card in line.split():
			cards.append(Card(values.find(card[0]) + 1, card[1]))
		if p054(cards[:5], cards[5:]):
			count += 1
	print(count)
