<?php

function p003($number) {
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
	echo p003(intval($argv[1])), "\n";
} else {
	echo "Usage: p003 <integer>\n";
	exit(1);
}

?>
