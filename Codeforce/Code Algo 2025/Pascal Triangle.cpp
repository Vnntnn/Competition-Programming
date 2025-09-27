// still wrong ans
#include <iostream>
using namespace std;

long long binomial(int n, int k) {
    if (k > n - k)
        k = n - k;
    long long res = 1;
    for (int i = 1; i <= k; ++i) {
        res *= (n - i + 1);
        res /= i;
    }
    return res;
}

int main() {
    int q;
    cin >> q;
    for (int i = 0; i < q; ++i) {
        int n, k;
        cin >> n >> k;
        cout << binomial(n, k) << endl;
    }
    return 0;
}