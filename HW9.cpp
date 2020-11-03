#include <iostream>

using namespace std;

//Christopher Marroquin
//12/1/18
//Objective: Vowel checker
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
        cout << "This character is in the alphabet. "<<"Your ASCII number is: " << ch << int(ch);
    }
    // If input doesn't met any requirements then it should cout what is written down below.
    else
    {
        cout << "This character is not a letter in the alphabet";
    }
    // if statement that checks if ch is a vowel or not
    if((ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U'))
    {
        cout << " and this letter is a vowel";
    }
    // I blanked the else statement because if it's not a vowel then the program will run the input like a regular letter.
    else {

         cout << " ";
    }
    return 0;
}
