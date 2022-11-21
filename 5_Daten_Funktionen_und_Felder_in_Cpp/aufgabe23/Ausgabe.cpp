#include <iostream>
using namespace std;

int main()
{
    int a = 10, b, c;

    a *= 5 + 10;
    cout << "a *=5 + 10: " << a << endl;

    a *= b = c = 20;
    cout << "a *= b = c = 20: " << a << endl;

    b = b == c;
    cout << "b = b == c:  " << b << endl;

    a >>= b + 2; // Division durch 2³ = 8
    cout << "a >>= b + 2: " << a << endl;

    a &= 0x3e;
    cout << "a &= 0x3e: " << a << endl;

    a = 3;
    b = 2;

    a *= b += a <<= a + b;
    cout << "a = " << a << ", b = " << b << endl;
}