#include <iostream>
#include <math.h>

using namespace std;

float numbery;
float numberx;
float area;
int counter;
int x;
string z;
int (Math);
float volume;


    int math()
    {
    cout << "Please input the height of your cylinder: ";
     cin >> numbery;
     cout << "Please enter the radius of your cylinder: ";
     cin >> numberx;
     //Area of cylinder
     area = 2*(3.14*numberx*numbery)+ 2*(3.14)* pow(numberx, 2.0);
     cout << "Your area is: " << area<< endl;
     volume = 3.14* pow (numberx, 2.0)*numbery;
     cout << "Your volume is: " <<volume<< endl;
     return 0;
    }


int main()
{
      cout << " Enter the amount of calculation wanted: ";
      cin >> counter;
      for ( x=0; x < counter; x++ )

       math();

    return 0;

}
