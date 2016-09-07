public class highlyDivisibleTriangularNumber {
    private int countDivisors(int n) {
        int c = 0;
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                c += 2; // i and n / i are factors
                if (n / i == i) c--; // removes duplicates for n = 1, n = i * i
            }
        }
        return c;
    }
    
    public int findTriangularNumber(int maxDivs) {
        int divs = 0;
        int n = 0;
        while (divs <= maxDivs) {
            n++;
            if (n % 2 == 0) divs = countDivisors(n / 2) * countDivisors(n + 1);
            else divs = countDivisors(n) * countDivisors((n + 1) / 2);
        }
        return n * (n + 1) / 2;
    }
    
    public static void main(String[] args) {
        highlyDivisibleTriangularNumber h = new highlyDivisibleTriangularNumber();
        System.out.println(h.findTriangularNumber(500));
    };
}
