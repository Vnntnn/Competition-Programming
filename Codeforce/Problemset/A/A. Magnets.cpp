#include <iostream>
using namespace std;

int main() {
    int n, cnt = 0, prev = 0;
    cin >> n;

    while (n--) {
        int curr;
        cin >> curr;
        if (prev != 0 && curr != prev) {
            cnt++;
        }
        if (n == 0 || prev == 0 && curr == prev) {
            cnt++;
        }
        prev = curr;
    }

    cout << cnt << endl;
    return 0;
}