public class p2 {
	public static int p2(int upper_bound) {
		if (upper_bound <= 2) return 0;

		int buffer[] = new int[] {0, 2},
			sum = 2,
			temp = 8;

		while (temp < upper_bound) {
			buffer[0] = buffer[1];
			buffer[1] = temp;
			sum += temp;
			temp = 4 * buffer[1] + buffer[0];
		}

		return sum;
	}

	public static void main(String[] args) {
		if (args.length == 1) {
			System.out.println(p2(Integer.parseInt(args[0])));
		} else {
			System.out.println("Usage: p2 <integer>");
			System.exit(1);
		}
	}
}
