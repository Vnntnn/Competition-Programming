#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> coins(n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> coins[i];
        total += coins[i];
    }

    sort(coins.rbegin(), coins.rend());

    int count = 0;
    long long taken = 0;
    for (int i = 0; i < n && taken * 2 <= total; ++i) {
        taken += coins[i];
        ++count;
    }

    cout << count << '\n';
    return 0;
}
