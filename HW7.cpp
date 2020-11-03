#include <iostream>

using namespace std;

// Christopher Marroquin
// 11/17/2018
// objective: Prime
int main()
{
 // Identify your variables
 int x, y;
  bool isPrime = true;
  //Prompt user
  cout << "Enter a positive integer: ";
  cin >> x;
// Prime checker formula
  for(y = 2; y <= x / 2; ++y)
  {
      if(x % y == 0)
      {
          isPrime = false;
          break;
      }
  }
  if (isPrime)
      cout << "This is a prime number";
  else
      cout << "This is not a prime number";

  return 0;
}
