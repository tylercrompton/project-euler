var p003 = function (number) {
	'use strict';

	if (number === 0) return Infinity;

	var i = 2,
		ceiling = Math.sqrt(Math.abs(number));
	while (i < ceiling) {
		for (i = 2; i <= ceiling; i += 1) {
			if (number % i === 0) {
				number /= i;
				break;
			}
		}
		ceiling = parseInt(Math.sqrt(Math.abs(number)));
	}
	return number;
}

if (arguments.length === 1) {
	println(p003(parseInt(arguments[0])));
} else {
	println('Usage: p003 <integer>');
	exit(1);
}
