(define
	divisible?
	(lambda
		(n divisor)
		(= 0 (modulo n divisor))))

(write
	(reduce-left
		+
		0
		(filter
			(lambda
				(n)
				(or
					(divisible? n 3)
					(divisible? n 5)))
			(iota 999 1))))

(newline)

