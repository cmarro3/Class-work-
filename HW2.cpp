#include <iostream>

using namespace std;

// Objective: Convert given time into Hour: Minute: Seconds: Millisecond
// 10/20/18
//Christopher Marroquin

//Define your variables
int hours = 60;
double seconds = 0.0166667;
double input;
int a;

int main()
{
cout << "Please enter how many minutes you want to convert: ";
cin >> input;

hours = input/60;
input = input - hours*60;

a = input/1;
input = input - a;

seconds = input/0.0166667;
input = input - seconds;
cout << hours << " hours " << a << " minutes " << seconds << " seconds " << endl;
















    return 0;
}
