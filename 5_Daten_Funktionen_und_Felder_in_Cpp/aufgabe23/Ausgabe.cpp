#include <iostream>
using namespace std;

int main()
{
    int a = 10, b, c;

    a *= 5 + 10;
    cout << a << endl;

    a *= b = c = 20;
    cout << a << ", " << endl;

    b = b == c;
    cout << b << endl;

    a >>= b + 2;
    cout << a << endl;

    a &= 0x3e;
    cout << a << endl;

    a = 3;
    b = 2;

    // a *= b += <<= a + b; - compiler error
    cout << "a= " << a << ", b= " << b << endl;
}