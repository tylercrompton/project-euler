def p029(lower_bound_a, upper_bound_a, lower_bound_b, upper_bound_b):
	return len({a ** b for b in range(lower_bound_b, upper_bound_b + 1) for a in range(lower_bound_a, upper_bound_a + 1)})

if __name__ == '__main__':
	print(p029(2, 100, 2, 100))