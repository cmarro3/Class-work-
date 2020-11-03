#include <iostream>
#include <stdlib.h>

using namespace std;

//defined global variables
string username1;
string username2;
string password1;
string password2;
string password3;
double balance;
int decision3;
//defined functions
void printIntroMenu();
void printMainMenu();
void start();
void login();
void createAccount();
void deposit();
void withdraw();
void requestbalance();
//main function greets and calls start function
int main()
{
    cout << " Hello! " << endl;
    start();
    return 0;
}
//code for the print intro menu
void printIntroMenu()
{
    //define variable used in function
    int decision1;
//question for user and taking input
    cout << " Please type 1 to login, 2 to Create an Account, or 3 to quit ";
    cin >> decision1;

    //if statement for the user decision
    if (decision1 == 1)
    {
        //calling function login
        login();
    }

    if (decision1 == 2)
    {
        //calling function createaccount
        createAccount();
    }

    if (decision1 == 3)
    {
        //ending the function and program
        exit (0);
    }

}
//code for the function ptintmainmenu
void printMainMenu()
{
    //defining variable
    int decision2;
//asking user second question and taking the input as decision2
    cout << " What would you like to do?: Type 1 to deposit money, Type 2 to withdraw money, Type 3 to request balance ";
    cin >> decision2;
//if statement for the users decision
    if ( decision2 == 1 )
    {
        //calling function deposit
        deposit();
    }

    if ( decision2 == 2 )
    {
        //calling function withdraw
        withdraw();
    }

    if ( decision2 == 3 )
    {
        //calling function requestbalance
        requestbalance();
    }

}

//code for function start
void start()
{
    //call function printintromenu
    printIntroMenu();
}
//code for function create account
void createAccount()
{
//ask user to enter username
    cout << " Please enter a username ";
    cin >> username1;
//ask user to enter password
    cout << " Please enter a password ";
    cin >> password1;
//ask user to reenter password
    cout << " Please reenter password ";
    cin >> password2;
//we want the 2 passwords that they input to be equivalent to each other
    if ( password1 == password2 )
    {
        //if passwords match then call the login function so the user can log in
        login();
    }
    //if the user types anything else then the function will state invalid and call the start function again
    else
    {
        cout << " Incorrect password ";
        start();
    }

 }
//code for the login function
void login()
{
//ask user to type in their username and password
    cout << " Input username ID ";
    cin >> username1;

    cout << " Input password ";
    cin >> password3;

//we need the password and user name that they created in the createaccount function to be equivalent to what they are using in the login function
    if ( username1 == username2, password1 == password3 )
    {
        //if they are equivalent then we want the program to call the printmainmenu function
        printMainMenu();
    }
}
//code for the deposit function
void deposit()
{
    //define variable used in function
    double amount;
//ask user how much they want to deposit and take the input amount which is the amount of money they would like to deposit
    cout << " How much money do you want to deposit? ";
    cin >> amount;
//equation to find the balance in account
    balance = balance + amount;
//display result
    cout << " $ " << balance;
//if the user would like to perform another transaction
    cout << " If you would like to perform another task type 1, if you would like to logout type 2 ";
    cin >> decision3;
//if the user wants to perform another transaction
      if (decision3 == 1)
    {
        //call printMainmenu function
        printMainMenu();
    }
//if the user wants to quit
    if (decision3 == 2)
    {
        exit (0);
    }


}
//code for withdraw function
void withdraw()
{
    //define variable
   double amount;
//ask question to user and take input as amount
    cout << " How much money would you like to withdraw? ";
    cin >> amount;
//if the balance is greater than 0 then the transaction can go through
    if ( balance > 0 )
    {


    balance = balance - amount;

    cout << " $ " << balance;
    }
    //if the transaction is less than 0 then the transaction cant go through
    else
    {

        cout << " Invalid Transaction ";
        //call the function printmainmenu so that the user can have a chance to deposit money to have in account
        printMainMenu();

    }

//if the user wants to perform another task
    cout << " If you would like to perform another task type 1, if you would like to logout type 2 ";
    cin >> decision3;

    if (decision3 == 1)
    {
        printMainMenu();
    }

     if (decision3 == 2)
    {
        exit (0);
    }

}
//code for function requestbalance
    void requestbalance()
{
//display the balance and ask user if they want to complete another transaction
    cout << " $ " << balance;
    cout << " If you would like to perform another task type 1, if you would like to logout type 2 ";
    cin >> decision3;

    if (decision3 == 1)
    {
        printMainMenu();
    }

    if (decision3 == 2)
    {
        exit (0);
    }
}
