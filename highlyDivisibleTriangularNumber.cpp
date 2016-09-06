#include <iostream>
using namespace std;

int countDivisors(int n) {
    c = 0;
    if (n == 1) c++;    // 1 is a factor
    else c += 2;        // 1 and n are factors
    if (n / sqrt(n) == sqrt(n)) c++; // sqrt(n) is a factor
    for (int i = 2; (int) floor(sqrt(n)); i++) {
        if (n % i == 0) c+= 2; // i and n / i are factors
    }
    return c;
}

int main() {
    return 0;
}
