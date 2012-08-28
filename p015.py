"""0, 0	1
0, 1	1
0, 2	1
0, 3	1
1, 1	2
1, 2	3
1, 3	4
2, 2	6
2, 3	10
3, 3	20


x	x	x	x

x	x	x	x

x	x	x	x

x	x	x	x"""

import functools as _functools
import sys as _sys

class memoize:
	"""A decorator for memoizing naïve functions.

Any function calls using keyword arguments will be ignored because doing otherwise **heavily** increases the CPU load."""

	def __call__(self, *args, **kwargs):
		if len(kwargs) == 0:
			try:
				return self._memos[args]
			except KeyError:
				result = self._function(*args)
				self._memos[args] = result
				return result
			except TypeError:
				return self._function(*args)
		else:
			return self._function(*args, **kwargs)

	def __init__(self, function):
		_functools.update_wrapper(self, function)
		self._memos = {}
		self._function = function

	def __repr__(self):
		'''Returns the function's docstring.'''
		return self.__class__.__name__ + '(' + self._function.__name__ + ')'

	def __get__(self, obj, objtype):
		'''Support instance methods.'''
		return _functools.partial(self.__call__, obj)

@memoize
def p015(width, height):
	if width == 0 or height == 0: return 1
	return p015(width - 1, height) + p015(width, height - 1)

if __name__ == '__main__':
	if len(_sys.argv) == 3:
		print(p015(int(_sys.argv[1]), int(_sys.argv[2])))
	else:
		print('Usage: p015 <integer> <integer>')
		_sys.exit(1)
