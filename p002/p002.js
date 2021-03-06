var p002 = function (upper_bound) {
	'use strict';

	if (upper_bound <= 2) {
		return 0;
	}

	var buffer = [0, 2],
		sum = 2,
		temp = 8;

	while (temp < upper_bound) {
		buffer[0] = buffer[1];
		buffer[1] = temp;
		sum += temp;
		temp = 4 * buffer[1] + buffer[0];
	}

	return sum;
};

if (arguments.length == 1) {
	println(p002(parseInt(arguments[0])));
} else {
	println('Usage: p002 <integer>');
	exit(1);
}
