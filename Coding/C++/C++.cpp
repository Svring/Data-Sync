#include <iostream>
using namespace std;

struct Student
{
    string name;
    string state;
    int age;
};

Student randomi(string state)
{
    Student s = {"Frankie", state, 5};
    return s;
}

int main(void)
{
    pair<int, string> you = {9, "Lumi"};
    cout << you.first << " " << you.second;
}