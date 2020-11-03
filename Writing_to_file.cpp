#include <iostream>
#include <fstream>
using namespace std;
//Christopher Marroquin
// 12/1/18
// Objective: Create and write to a file in c++
int main()
{
    // NOTE: Before writing/creating to a file make sure you chosen the desired path in code blocks before making a file.
    // Include the <fstream> in order to open and write a file.
    // ofstream myfile means the file I will create will treated like an object
    ofstream myfile;
    // myfile.open justs opens the file up and whatever is in the parentheses you can name and add a file type
    myfile.open("new file.txt");
    // myfile << is treated like a cout, but whatever is in the parentheses will be printed in file not the terminal.
    myfile << "I just wrote to a file in c++ .\n"<< endl;
    myfile << "Hello, World!"<<endl;
    myfile << "Red, Blue, Green, Yellow, Pink, Orange"<<endl;
    // always close your flies to flush whatever cache was left.
    // CONGRATS you should have a file on your desktops with what you wrote to it!
    myfile.close();
    return 0;
}
