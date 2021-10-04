
import java.util.stream.IntStream;


/**
 * This thing will sum up multiples of three or five between 3 and MAX_VALUE
 */
public class ThreeOrFiveStreamed {

    private static int MAX_VALUE = 1000;

    public static void main(String[] args) {

        System.out.println(IntStream.range(3, MAX_VALUE)
            .filter(i -> i % 3 == 0 || i % 5 == 0)
            .sum());
    }
}