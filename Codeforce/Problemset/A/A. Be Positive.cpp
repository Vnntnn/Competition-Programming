#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    while (n--) {
        int an, cnt = 0, sum = 0;
        cin >> an;
        int arr[an];
        for (int i = 0; i < an ; i++) {
            cin >> arr[i];
            if (arr[i] == 0) {
                cnt++;
                arr[i] = 1;
            }
            sum *= arr[i];
        }
        // if (sum <= 0) {
        //     while (1) {
        //     }
        // }
        cout << sum << endl;
        cnt = 0;
    }
    return 0;
}