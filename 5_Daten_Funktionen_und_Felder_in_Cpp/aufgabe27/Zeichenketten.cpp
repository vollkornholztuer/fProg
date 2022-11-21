#include <iostream>

void strcpy1(char *s, char *t)
{
    int i = 0;
    while (t[i] = s[i]) // Loesung 2022.11.21
    {
        i++;
    }
}

void strcpy2(char *s, char *t)
{
    while (*t++ = *s++) // Loesung 2022.11.21
    {
        s++;
        t++;
    }
}

int main()
{
    char quelle[40] = "Das ist unser Text!";
    char ziel1[40];
    char ziel2[40];

    strcpy1(quelle, ziel1)
    {
        std::cout << "Ergebnis 1: \"" << ziel1 << "\"\n";
    }

    strcpy2(quelle, ziel2)
    {
        std::cout << "Ergebnis 2: \"" << ziel2 << "\"n";
    }
    return 0;
}