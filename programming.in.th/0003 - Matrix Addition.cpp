#include <bits/stdc++.h>
using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    
    vector<vector<int>> mat1(m, vector<int>(n));
    vector<vector<int>> mat2(m, vector<int>(n));
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> mat1[i][j];
        }
    }
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int val;
            cin >> val;
            cout << mat1[i][j] + val;
            if (j < n - 1) cout << " ";
        }
        cout << "\n";
    }
    
    return 0;
}
