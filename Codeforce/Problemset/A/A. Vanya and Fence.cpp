#include <iostream>
using namespace std;

int main() {
    int n, h, res = 0;
    cin >> n >> h;
    for (int i = 0; i < n; i++) {
        int n;
        cin >> n;
        res += n > h ? 2 : 1;
    }
    cout << res << endl;
    return 0;
}