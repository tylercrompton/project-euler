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
def fib(n):
	if n == 0 or n == 1: return n
	else: return fib(n - 1) + fib(n - 2)

def p025(digit_count):
	i = 0
	while len(str(fib(i))) != digit_count:
		i += 1
	return i

if __name__ == '__main__':
	if len(_sys.argv) == 2:
		print(p025(int(_sys.argv[1])))
	else:
		print('Usage: p025 <integer>')
		_sys.exit(1)
