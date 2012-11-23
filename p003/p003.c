#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

long long int p003(long long int number) {
	if (number == 0) return LLONG_MAX;

	int i = 0;
	double ceiling = floor(sqrt(llabs(number)));
	while (i < ceiling) {
		for (i = 2; i <= ceiling; i++) {
			if (number % i == 0) {
				number /= i;
				break;
			}
		}
		ceiling = floor(sqrt(llabs(number)));
	}
	return (long long int) number;
}

int main(int argc, char * argv[]) {
	if (argc == 2) {
		printf("%lld\n", p003(atoll(argv[1])));
	} else {
		printf("Usage: p003 <integer>\n");
		return 1;
	}
}
