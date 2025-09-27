#include <iostream>
using namespace std;

int main() {
    int grid, count = 0;
    cin >> grid;

    while (1) {
        if (grid <= 1) {
            break;
        }

        if (grid % 2 != 0) {
            if (grid >= 5) {
                grid -= 5;
            }
            else if (grid >= 3 && grid < 5) {
                grid -= 3;
            }
            else if (grid >= 1 && grid < 3) {
                grid -= 1;
            }
        }
        else {
            if (grid >= 6) {
                grid -= 6;
            }
            else if (grid >= 5 && grid < 6) {
                grid -= 5;
            }
            else if (grid >= 4 && grid < 5) {
                grid -= 4;
            }
            else if (grid >= 3 && grid < 4) {
                grid -= 3;
            }
            else if (grid >= 2 && grid < 3) {
                grid -= 2;
            }
            else if (grid >= 1 && grid < 3) {
                grid -= 1;
            }
        }
        count += 1;
    }

    cout << count << endl;

    return 0;
}