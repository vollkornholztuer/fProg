#include <iostream>
#include <cstring>

using namespace std;

int main(int argc, char *argv[])
{

    char **pp, *z;
    if (argc > 1)
    {
        pp = argv + 1;
        z = *pp + strlen(*pp); // *pp - dereferenzieren vom Zeiger auf Array (von zwei Stern auf ein Stern)

        while (*pp - --z) // <==> while(*pp - --z!=0) <==> while(--z!=*pp)
            cout << --*z;

        // D --> C
        // P --> O
        // C --> B
        // V --> U
        //

        cout << *z << endl;
    }
    return 0;
}