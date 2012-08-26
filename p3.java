import java.lang.Math;
import java.lang.Math;
import java.lang.Math;

public class p3 {
	public static float p3(float number) {
		if (number == 0) return Float.POSITIVE_INFINITY;

		int i = 0;
		float ceiling = (float) Math.floor(Math.sqrt(Math.abs(number)));
		while (i < ceiling) {
			for (i = 2; i <= ceiling; i++) {
				if (number % i == 0) {
					number /= i;
					break;
				}
			}
			ceiling = (float) Math.floor(Math.sqrt(Math.abs(number)));
		}
		return (float) number;
	}

	public static void main(String[] args) {
		if (args.length == 1) {
			System.out.printf("%.0f\n", p3(Float.parseFloat(args[0])));
		} else {
			System.out.println("Usage: p3 <integer>");
			System.exit(1);
		}
	}
}
