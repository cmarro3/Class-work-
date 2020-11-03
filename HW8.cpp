#include <iostream>

using namespace std;

// Christopher Marroquin
// 11/24/18
// objective: using designed program, check weather the input character is in the alphabet.
int main()
{
    // You must create a char variable so then you can input letters
    char ch;
    //Prompt user
    cout << "Hello, please enter a character: ";
    cin >> ch;
    // Create an if else loop, and set the testing variables between A to Z and set a logical ore in order to check the users character.
    if (( ch>= 'a'&&ch<='z'  ) || (ch>= 'A'&&ch<='Z'))
    {
        cout<< "This character is a alphabet";
    }
    // If input doesn't met any requirements then it should cout what is written down below.
    else
    {
        cout << "This character is not an alphabet";
    }
    return 0;
}
