#include <iostream>

string &strToUpper(const string &s1)
{

    string s2;
    s2 = " ";

    for (int i = 0; i < s1.length(); i++)

        s2 += toupper(s1[i]);

    return s2;
}

int main()
{
    string testString = "Pizza";
    strToUpper(testString);
}