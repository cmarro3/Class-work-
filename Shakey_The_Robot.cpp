#include <iostream>
using std::endl;
using std::cout;
using std::cin;
#include <string>
using std::string;
#include<Windows.h>
#include<conio.h>

//Christopher Marroquin
//Jorge Carranza
//Jacob Salazar
// 12/15/18
//Objective: Create Shakey the game

//Define global variables so that they can be used in all functions
void welcome();
char getKeyPress();
void printLevel(int);
void setMe(int);
bool isExit(int, int, int);
bool isWall(int, int, int);
int getPos(int, int&);
int getX(int, int &);
void update(int, int, int);
void makeSpace(int, int, int);

//Create the space that shakey can move within (garden)
const char space = ' ';
const char me = '@';
char lvl1[20][20] = { { '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { 'X', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', 'O' },
                    { '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' } };

char lvl2[20][20] = { { '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', 'O' },
                    { '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#' },
                    { '#', '#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' },
                    { '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#' },
                    { 'X', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#' },
                    { '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' } };

//main functions that begin the game and take input which level the user wants to play
int main(void){
begin:
    system("CLS");
    cout << "\n\n\n\n\n\n\n    \t\t\t";
    cout << "PLEASE SELECT A LEVEL (Press 0 to exist) \n\n    \t\t\t1---2\n    \t\t\t";
    int lvl;
    cin >> lvl;
    if (lvl != 2 && lvl != 1 && lvl == 0){
            cout<< "Goodbye! Have a good day";
            return 0;
    }
    //calling functions to start the game
    system("CLS");
    setMe(lvl);
    printLevel(lvl);
    int x, y;
//when the user chooses the level they want to play, we start the function getkeypress
    while (1){

        char move = getKeyPress();

        switch (move){
//for the case of the first level we are creating where shakey will begin and creating the walls and exit
        case 'u':
            x = getPos(lvl, y);
            if (!isWall(x - 1, y, lvl)){
                if (isExit(x - 1, y, lvl)){
                    system("CLS");
                    //output you win when the user gets shakey to the end of the level
                    cout << "You Win!" << endl;
                    //delay when the game is won so that the user can see that they won the game
                    Sleep(1000);
                    //function that takes user back to the beginning of the program
                    goto begin;;
                }
                system("CLS");
                makeSpace(lvl, x, y);
                update(lvl, x - 1, y);
            }
            break;
            //case of the second level creating where shakey begins and creating the walls and exit
        case 'd':
            x = getPos(lvl, y);
            if (!isWall(x + 1, y, lvl)){
                if (isExit(x + 1, y, lvl)){
                    system("CLS");
                    cout << "You Win!" << endl;
                    Sleep(1000);
                    goto begin;;
                }
                system("CLS");
                makeSpace(lvl, x, y);
                update(lvl, x + 1, y);
            }
            break;
        case 'l':
            x = getPos(lvl, y);
            if (!isWall(x, y - 1, lvl)){
                if (isExit(x, y - 1, lvl)){
                    system("CLS");
                    cout << "You Win!" << endl;
                    Sleep(1000);
                    goto begin;;
                }
                system("CLS");
                makeSpace(lvl, x, y);
                update(lvl, x, y - 1);
            }
            break;
        case 'r':
            x = getPos(lvl, y);
            if (!isWall(x, y + 1, lvl)){
                if (isExit(x, y + 1, lvl)){
                    system("CLS");
                    cout << "You Win!" << endl;
                    Sleep(1000);
                    goto begin;;
                }
                system("CLS");
                makeSpace(lvl, x, y);
                update(lvl, x, y + 1);
            }
            break;
        default:
            break;
        }

    }

    return 0;
}

//print level function that displays the maze
void printLevel(int lvl){
    cout << "\n\n\n\n\n";
    //if the user types 1 to choose the level
    if (lvl == 1){
            //x values can range based on the size of the maze
        for (int i = 0; i != 15; ++i){
            cout << endl << "\t\t\t\t";
            for (int j = 0; j != 15; ++j){
                cout << lvl1[i][j];
            }
        } cout << endl;
    }
    //if user types 2 to choose the level
    if (lvl == 2){
            //y values can range based on the size of the maze
        for (int i = 0; i != 15; ++i){
            cout << endl << "\t\t\t\t";
            for (int j = 0; j != 15; ++j){
                cout << lvl2[i][j];
            }
        } cout << endl;
    }

}
//set me function is used to create where shakey will begin in the maze for level 1
void setMe(int lvl){
    int x, y;
    if (lvl == 1){
        x = getX(lvl, y);
        lvl1[x][y] = me;
    }
    //create where shakey will begin in level 2
    if (lvl == 2){
        x = getX(lvl, y);
        lvl2[x][y] = me;
    }
}
//got this function from a CPP forum
char getKeyPress(){

    char key = 127;

    key = _getch();
//ASCII value for the arrow keys on the keyboard used to move shakey within the maze
    if (key == 0 || key == -32){

        key = _getch();

        if (key == 72) {
            key = 'u';
        } else if (key == 75){
            key = 'l';
        } else if (key == 77){
            key = 'r';
        } else if (key == 80){
            key = 'd';
        }
    }
    return key;
}

bool isExit(int x, int y, int lvl){
    //Creating where the exit will be in level 1
    if (lvl == 1){
        if (lvl1[x][y] == 'O'){
            return true;
        }
        else {
            return false;
        }
    }
    //Creating where the exit will be in level 2
    if (lvl == 2){
        if (lvl2[x][y] == 'O'){
            return true;
        }
        else {
            return false;
        }
    }
    return true;

}
//This is how shakey is moving so in level 1 an i value can range from 0-? based on the size of the maze and we set the values of x and y equal to the @ which is used to symbolize shakey
int getPos(int lvl, int &y){
    int xCoord;
    if (lvl == 1){
        for (int i = 0; i != 15; ++i){
            for (int j = 0; j != 15; ++j){
                if (lvl1[i][j] == '@'){
                    xCoord = i;
                    y = j;
                    return xCoord;
                }
            }
        }
    }
    //This is how shakey is moving so in level 2 an i value can range from 0-? based on the size of the maze and we set the values of x and y equal to the @ which is used to symbolize shakey
    if (lvl == 2){
        for (int i = 0; i != 15; ++i){
            for (int j = 0; j != 15; ++j){
                if (lvl2[i][j] == '@'){
                    xCoord = i;
                    y = j;
                    return xCoord;
                }
            }
        }
    }
    return 0;
}
//to create the walls, we set up the function iswall
bool isWall (int x, int y, int lvl){
    if (lvl == 1){
            //if the user wants to move into the symbol of a wall which is a hashtag, then we print an invalid move prompt so that the user knows he cant move in that direction
        if (lvl1[x][y] == '#'){
            cout << "\n\t\t\tCannot move! That is a wall / boundary.";
            Sleep(400);
            system("CLS");
            printLevel(lvl);
            return true;
        }
        else {
            return false;
        }
    }
    //if the user wants to move into the symbol of a wall which is a hashtag, in level 2, then we print an invalid move prompt so that the user knows he cant move
    if (lvl == 2){
        if (lvl2[x][y] == '#'){
            cout << "\n\t\t\tCannot move! That is a wall / boundary.";
            Sleep(400);
            system("CLS");
            printLevel(lvl);
            return true;
        }
        else {
            return false;
        }
    }
    return true;
}

int getX(int lvl, int &y){
    int xCoord;
    if (lvl == 1){
            //the for loop within the for loop creates the x and y values for shakey when it is moving
        for (int i = 0; i != 15; ++i){
            for (int j = 0; j != 15; ++j){
                if (lvl1[i][j] == 'X'){
                    xCoord = i;
                    y = j;
                    return xCoord;
                }
            }
        }
    }
    //the for loop within the for loop creates the x and y values for shakey when it is moving within level 2
    if (lvl == 2){
        for (int i = 0; i != 15; ++i){
            for (int j = 0; j != 15; ++j){
                if (lvl2[i][j] == 'X'){
                    xCoord = i;
                    y = j;
                    return xCoord;
                }
            }
        }
    }
    return 0;
}
void update(int lvl, int x, int y){
    if (lvl == 1){
        lvl1[x][y] = me;
        printLevel(lvl);
    }
    if (lvl == 2){
        lvl2[x][y] = me;
        printLevel(lvl);
    }
}

//the function makespace is the path shakey can move within
void makeSpace(int lvl, int x, int y){
    if (lvl == 1){
        lvl1[x][y] = space;
    }
    if (lvl == 2){
        lvl2[x][y] = space;
    }
}
