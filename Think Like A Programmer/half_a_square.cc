#include <iostream>
using std::cin;
using std::cout;


int main() {

    for (int row = 0; row < 5; row++) {
        for (int col = 0; col < 5 - row; col++)
        {
                cout << "#";           
        }
        cout << "\n";
    }
    return 0;
}
