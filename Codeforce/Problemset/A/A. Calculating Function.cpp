#include <iostream>
using namespace std;

long long cal_func(long long n) {
    if (n % 2 == 0) return n / 2;
    else return - (n + 1) / 2;
}

int main(void) {
    long long n;
    cin >> n;
    cout << cal_func(n) << '\n';
    return 0;
}