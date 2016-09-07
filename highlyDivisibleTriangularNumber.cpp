#include <iostream>
#include <math.h>

using namespace std;

int countDivisors(int n) {
    int c = 0;
    if (n == 1) return 1;    // 1 is a factor
    else c += 2;        // 1 and n are factors
    int sq = ceil(sqrt(n));
    if ((n / sq) == sq) c++; // sqrt(n) is a factor
    for (int i = 2; i < sq; i++) {
        if (n % i == 0) c+= 2; // i and n / i are factors
    }
    return c;
}

int main() {
    int maxDivs = 500;
    int divs = 0;
    int n;
    for (n = 2; divs <= maxDivs; n++) {
        if (n % 2 == 0) divs = countDivisors(n / 2) * countDivisors(n + 1);
        else divs = countDivisors(n) * countDivisors((n + 1) / 2);
    }
    cout << n << " " << divs << endl;
    cout << (n * (n + 1) / 2) << endl;
    return 0;
}
