#include <iostream>
using std::cin;
using std::cout;


int main() {

    for (int row = 0; row < 8; row++) {
        for (int col = 0; col < 4 - abs(4 -row); col++)
        {
                cout << "#";           
        }
        cout << "\n";
    }
    return 0;
}
/*

row desired    4-abs(4-row)    diff
1      1        3          
2      2        2      
3      3        1      
4      4        0      
5      3       -1   
6      2       -2     
7      1       -3         

*/
