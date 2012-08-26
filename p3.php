<?php

function p3($number) {
	if ($number == 0) return Infinity;

	$i = 0;
	$ceiling = floor(sqrt(abs($number)));
	while ($i < $ceiling) {
		for ($i = 2; $i <= $ceiling; $i++) {
			if ($number % $i == 0) {
				$number /= $i;
				break;
			}
		}
		$ceiling = floor(sqrt(abs($number)));
	}
	return $number;
}

if (count($argv) == 2) {
	echo p3(intval($argv[1])), "\n";
} else {
	echo "Usage: p3 <integer>\n";
	exit(1);
}

?>
