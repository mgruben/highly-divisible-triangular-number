#include <iostream>

using namespace std;

int countDivisors(int n) {
    int c = 0;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            c+= 2; // i and n / i are factors
            if (n / i == i) c--; // removes duplicates for n = 1, n = i * i
        }
    }
    return c;
}

int main() {
    int maxDivs = 500;
    int divs = 0;
    int n;
    for (n = 1; divs <= maxDivs; n++) {
        if (n % 2 == 0) divs = countDivisors(n / 2) * countDivisors(n + 1);
        else divs = countDivisors(n) * countDivisors((n + 1) / 2);
    }
    n--; // we overshoot by one in the above for loop
    cout << "The first triangular number with more than " <<
    maxDivs << " divisors is " << (n * (n + 1) / 2) << " (" << divs << 
    " divisors)" << endl;
    return 0;
}
