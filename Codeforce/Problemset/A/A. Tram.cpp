#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int sum = 0, max = 0;
    for (int i = 0; i < n; i++) {
        int out, in;
        cin >> out >> in;
        sum = sum - out + in;
        if (sum > max) max = sum;
    }
    cout << max << endl;
    return 0;
}