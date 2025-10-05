#include <iostream>
using namespace std;

int main() {
    int n, cnt = 0;
    cin >> n;


    for (int i = 0; i < n; i++) {
        int t, c;
        cin >> t >> c;
        if (c - t >= 2) cnt++;
    }
    cout << cnt << endl;
    return 0;
}