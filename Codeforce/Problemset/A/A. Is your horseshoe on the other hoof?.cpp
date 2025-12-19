#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> nums;

    for (int i = 0; i < 4; i++) {
        int num;
        cin >> num;

        bool found = false;
        for (int x : nums) {
            if (x == num) {
                found = true;
                break;
            }
        }
        if (!found) nums.push_back(num);
    }

    cout << 4 - nums.size() << "\n";
    return 0;
}

