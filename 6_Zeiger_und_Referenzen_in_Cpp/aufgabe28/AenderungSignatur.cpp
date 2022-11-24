#include <iostream>

char &strToUpper(const char[] & s1)
{

    char s2[s1.length() / 1] = {a}; // char = 1 byte, deshalb durch 1 geteilt
    // s2 = " ";

    for (int i = 0; i < s1.length(); i++)

        s2 += toupper(s1[i]);

    return s2;
}

int main()
{
    string testString = "Pizza";
    strToUpper(testString);
    std::cout << testString << std::endl;
}