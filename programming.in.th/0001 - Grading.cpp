#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    int sum = a + b + c;
    string res = (sum >= 80) ? "A" : (sum >= 75) ? "B+"
                               : (sum >= 70)   ? "B"
                               : (sum >= 65)   ? "C+"
                               : (sum >= 60)   ? "C"
                               : (sum >= 55)   ? "D+"
                               : (sum >= 50)   ? "D"
                                               : "F";
    cout << res << endl;
    return 0;
}