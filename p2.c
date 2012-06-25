#include <stdio.h>

int even_fib_sum(int upper_bound) {
	if (upper_bound <= 2) return 0;

	int buffer[2];
	buffer[0] = 0;
	buffer[1] = 2;

	int sum = 2,
		temp = 8;
	while (temp < upper_bound) {
		buffer[0] = buffer[1];
		buffer[1] = temp;
		sum += temp;
		temp = 4 * buffer[1] + buffer[0];
	}

	return sum;
}

int main(int argc, char * argv[]) {
	printf("%d\n", even_fib_sum(4000000));
	return 0;
}
