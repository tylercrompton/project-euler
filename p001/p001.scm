(define (divisible? n divisor) (= (modulo n divisor) 0))

(write
	(reduce-left + 0
		(filter
			(lambda (n) (or
				(divisible? n 3)
				(divisible? n 5)))
			(iota 999 1))))

(newline)
