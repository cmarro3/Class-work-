#include <iostream>
#include <string>
#include "student.h"
using namespace std;

int main()
{
    Student person1;

    string firstName;
    string lastName;
    int age;
    //double gpa;
    //char curGrade;
    //string curClass;

    cout<< "Hello, please enter first name: ";
    cin >> firstName;
    cout<< "Enter last name: ";
    cin >> lastName;
    cout<< "Enter your age: ";
    cin >> age;

    person1.setfName(firstName);


    return 0;
}
