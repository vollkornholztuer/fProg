#include <iostream>

int main()
{
    int n = 3;
    float a = 0, b = 3.2;
    int m;
    char c, e = 1;

    // Beispielausdruck
    m = ~(~0 << 1);
    std::cout << "m = ~(~0 << 1); = " << m << std::endl;

    // Ausdrücke
    m = n % 2 ? -1 + n : n;
    std::cout << "m = n % 2 ? -1 + n : n; = " << m << std::endl;
    m = (n % 2) ? (-1 + n) : n;
    std::cout << "m = (n % 2) ? (-1 + n) : n; = " << m << std::endl;

    std::cout << "" << std::endl;

    a = 1 / 2 * b;
    std::cout << "a = 1 / 2 * b; = " << a << std::endl;
    a = 1 / (2 * b);
    std::cout << "a = 1 / (2 * b); = " << a << std::endl;

    std::cout << "" << std::endl;

    c = 4 < 1 << n;
    std::cout << "c = 4 < 1 << n; = " << c << std::endl;
    c = (4 < 1) << n;
    std::cout << "c = (4 < 1) << n; = " << c << std::endl;
    c = 4 < (1 << n);
    std::cout << "c = 4 < (1 << n); = " << c << std::endl;
    c = (4 < 1 << n);
    std::cout << "c = (4 < 1 << n); = " << c << std::endl;

    std::cout << "" << std::endl;

    c = 1 / e / b + a;
    std::cout << "c = 1 / e / b + a; = " << c << std::endl;
    c = (1 / e) / b + a;
    std::cout << "c = (1 / e) / b + a; = " << c << std::endl;
    c = 1 / (e / b) + a;
    std::cout << "c = 1 / (e / b) + a; = " << c << std::endl;
    c = 1 / e / (b + a);
    std::cout << "c = 1 / (e / b) + a; = " << c << std::endl;
    c = (1 / e / b + a);
    std::cout << "c = (1 / e / b + a); = " << c << std::endl;
}
