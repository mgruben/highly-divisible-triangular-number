#include <iostream>
#include <math.h>

using namespace std;

int countDivisors(int n) {
    int c = 0;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            c+= 2; // i and n / i are factors
            if (n / i == i) c--;
        }
    }
    return c;
}

int main() {
    int maxDivs = 500;
    int divs = 0;
    int n;
    for (n = 10; divs <= maxDivs; n++) {
        if (n % 2 == 0) divs = countDivisors(n / 2) * countDivisors(n + 1);
        else divs = countDivisors(n) * countDivisors((n + 1) / 2);
        cout << n << " " << divs << endl;
    }
    cout << (n * (n + 1) / 2) << endl;
    return 0;
}
