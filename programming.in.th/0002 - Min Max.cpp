#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int min, max;
    
    for(int i = 0; i < n; i++) {
        int num;
        cin >> num;
        if (i == 0) {
            min = max = num;
        } else {
            min = (num < min) ? num : min;
            max = (num > max) ? num : max;
        }
    }
    cout << min << '\n' << max << endl;
    return 0;
}