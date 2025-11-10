#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int y;
    cin >> y;
    while (true) {
        ++y;
        string s = to_string(y);
        set<char> st(s.begin(), s.end());
        if (st.size() == s.size()) {
            cout << y << '\n';
            break;
        }
    }
    return 0;
}