
#include <iostream>

using namespace std;

// Christopher Marroquin
// 10/13/2018
// Objective: Convert given amount into dollars and cents


// Define your variables of currency
int dollars;
int pennies = 1;
int nickels = 5;
int dimes = 10;
int quarters = 25;
int input;

int main()
{
// Ask for input of cents
cout << "Enter amount of dollars and cents: ";
cin >> input;
dollars = input/100;
input = input - dollars*100;
cout << " You have " << dollars << " dollars " ;
quarters = input/25;
input = input - quarters*25;
cout << " You have " << quarters << " quarters " ;
cout << " You have " << input/dimes << " dimes " ;
dimes = input/10;
input = input - dimes *10;
cout << " You have " << input/nickels << " nickels " ;
nickels = input/5;
input = input - nickels*5;
cout << " You have " << input/pennies << " pennies " ;
pennies = input;
    return 0;
}
