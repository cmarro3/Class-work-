#include <iostream>
using namespace std;

//Chirstopher Marroquin
//12/01/2018
// Objective: Create a leap year converter with given perimeters.

// I created a function in order for me to create a for loop for my counter.
int leapYear();

leapYear()

   {
    // I declared my variables in my scope
    int yr;
    // Added color to the text for a little flare
    system ("color A");
    cout << "Hello, please enter year: ";
    cin >> yr;
    // I added the % module in order for to test the remainder
    if ((yr%100!=0)&&(yr%4==0))
    {
        cout << "This is a leap year"<<endl;
    }

else if((yr%100==0) && (yr%400==0))
	{
		cout<<"This is a Leap Year"<<endl;
	}
	else if(yr%400==0)
	{
		cout<<"This is a Leap Year"<<endl;
	}
	else
	{
		cout<<"This is not a Leap Year"<<endl;
	}
	return 0;
}


int main()
{
// declared variables
int x;
int counter;
 // same light green color
 system( "color A");
 cout << "Enter the amount of years you're checking: ";
 cin >> counter;
   for ( x=0; x < counter; x++ )
// Called my created function
leapYear();
    return 0;
}
