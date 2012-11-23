def triangles():
	n = 1
	while True:
		yield n * (n + 1) // 2
		n += 1

def pentagons():
	n = 1
	while True:
		yield n * (3 * n - 1) // 2
		n += 1

def hexagons():
	n = 1
	while True:
		yield n * (2 * n - 1)
		n += 1

def p045():
	triangles_ = triangles()
	pentagons_ = pentagons()
	hexagons_ = hexagons()

	h = p = t = 0
	while True:
		h = next(hexagons_)
		p = next(pentagons_)
		while p < h:
			p = next(pentagons_)
		t = next(triangles_)
		while t < h:
			t = next(triangles_)
		if t == h == p and t not in (1, 40755):
			return t

if __name__ == '__main__':
	print(p045())
