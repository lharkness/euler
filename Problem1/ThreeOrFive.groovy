class ThreeOrFive {
    static final int MAX_VALUE = 1000;
    static void main(String[] args) {
        int total = 0;
        for (int i = 1; i < MAX_VALUE; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                total += i;
            }
        }
        println(total);
    }
}