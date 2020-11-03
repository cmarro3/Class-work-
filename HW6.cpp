#include <iostream>

using namespace std;
int numb;

int main()
{
    cout << "Please enter a integer: ";
    cin >> numb;
    if ( numb % 2 == 0)
        cout << numb << " is even.";
    else
        cout << numb << " is odd.";
    return 0;
}
