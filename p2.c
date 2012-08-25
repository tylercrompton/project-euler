#include <stdio.h>

int p2(int upper_bound) {
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
	if (argc == 2) {
		printf("%d\n", p2(atoi(argv[1])));
		return 0;
	}
	printf("Usage: p2 <integer>\n");
	return 1;
}
