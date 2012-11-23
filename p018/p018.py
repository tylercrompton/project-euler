import sys as _sys

def tree_permutations(iterables):
	def _tree_permutations(iterables, i):
		if len(iterables):
			for permutation in _tree_permutations(iterables[1:], i):
				yield (iterables[0][i],) + permutation
			for permutation in _tree_permutations(iterables[1:], i + 1):
				yield (iterables[0][i],) + permutation
		yield ()
	return _tree_permutations(iterables, 0)

if __name__ == '__main__':
	tree = [tuple(map(int, line.split())) for line in _sys.stdin.readlines()]
	print(sum(max(tree_permutations(tree), key=sum)))
