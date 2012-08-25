#include <stdio.h>

unsigned int p1(int max) {
	unsigned int i = 0,
		total = 0;

	while (i < max) {
		if (i + 15 < max)
			total += i * 7 + 60;
		else if (i + 12 < max)
			total += i * 6 + 45;
		else if (i + 10 < max)
			total += i * 5 + 33;
		else if (i + 9 < max)
			total += i * 4 + 23;
		else if (i + 6 < max)
			total += i * 3 + 14;
		else if (i + 5 < max)
			total += i * 2 + 8;
		else if (i + 3 < max)
			return total + i + 3;
		i += 15;
	}

	return total;
}

int main(int argc, char * argv[]) {
	if (argc == 2) {
		printf("%d\n", p1(atoi(argv[1])));
		return 0;
	}
	printf("Usage: p1 <integer>\n");
	return 1;
}
