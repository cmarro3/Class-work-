//Christopher Marroquin
// 10/28/18
//Objective: convert temperature to fahrenheit to celsius

#include <iostream>
using namespace std;

int convertToCelsius(float);
int convertToCelsius(float degrees)
{
    char a;
    float degreesc;
    float degreesf;

    cout << " Is this fahrenheit or celsius ( f for fahrenheit, c for celsius )";
    cin >> a;

    if ( a == 'f')
    {
    degreesc = ( degrees - 32 ) * .555555555556;

    cout << degreesc << " Degrees in celsius " << endl;
    }
    else if ( a == 'c')
    {
        degreesf = (degrees * 1.8) + 32;
    cout << degreesf << " Degrees in fahrenheit " <<endl;

    }
    else{
        cout << " Invalid type f or c " << endl;
    }
    return (0);
}



int main()
{
    int x;
    int counter;
    float a;
    cout << " Enter the amount of conversions needed ";
    cin >> counter;
for ( x=0; x < counter; x++ )

{
    cout << " Enter the temperature in degrees ";
    cin >> a;
    convertToCelsius(a);
}
}
