#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int lucky[] = {4,7,44,47,74,77,444,447,474,477,744,747,774,777};
    for (int d : lucky) {
        if (n % d == 0) {
            cout << "YES\n";
            return 0;
        }
    }
    cout << "NO\n";
    return 0;
}