#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;

    string target = "hello";
    int j = 0;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == target[j]) {
            j++;
        }
        if (j == target.length()) {
            break;
        }
    }

    cout << (j == target.length() ? "YES" : "NO") << '\n';

    return 0;
}