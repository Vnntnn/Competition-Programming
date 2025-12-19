#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int u = 0, l = 0;
    for (char ch : s) {
        int ascii = (int) ch;
        if (ascii >= 65 && ascii <= 90) u++;
        if (ascii >= 97 && ascii <= 122) l++;
    }
    string r = (u == s.length()) ? "All Capital Letter" : (l == s.length()) ? "All Small Letter" : "Mix";
    cout << r << endl;
    return 0;
}