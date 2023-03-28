#include <iostream>

using namespace std;

int main()
{
    char digit;

    cout << "Enter a one-digit number: ";
    cin >> digit;
    // digit = cin.get();

    int sum = digit - '0';
    cout << "Is the sum of digits " << sum << "? \n";
}