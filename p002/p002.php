<?php

function p002($upper_bound) {
	if ($upper_bound <= 2) return 0;

	$buffer = array(0, 2);
	$sum = 2;
	$temp = 8;

	while ($temp < $upper_bound) {
		$buffer[0] = $buffer[1];
		$buffer[1] = $temp;
		$sum += $temp;
		$temp = 4 * $buffer[1] + $buffer[0];
	}

	return $sum;
}

if (count($argv) == 2) {
	echo p002(intval($argv[1])), "\n";
} else {
	echo "Usage: p002 <integer>\n";
	exit(1);
}

?>
