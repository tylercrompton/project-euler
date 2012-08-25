public class p1 {
	public static int p1(int max) {
		int i = 0,
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

	public static void main(String[] args) {
		if (args.length == 1) {
			System.out.println(p1(Integer.parseInt(args[0])));
		} else {
			System.out.println("Usage: p1 <integer>");
			System.exit(1);
		}
	}
}
