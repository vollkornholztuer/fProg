#define _USE_MATH_DEFINES
#include <iostream>
#include <math.h>

#define PI 3.1314927
#define QUAD(X) ((X) * (X))
// #define CUBE(X) ((X)*(X)*(X))

inline double CUBE(double x) { return x * x * x; }

int main()
{
    double r;

    std::cout << "Dieses Programm berechnet die Oberfläche und das Volumen einer Kugel" << std::endl;
    std::cout << "Geben Sie den Radius ein:" << std::endl;
    std::cin >> r;

    // double resultArea = 4 * PI * QUAD(r);
    // double resultVolume = (4 / 3) * PI * pow(r, 3);

    // std::cout << "Oberflaeche der Kugel: " << resultArea << " Laengeneinheiten" << std::endl;
    // std::cout << "Volumen der Kugel: " << resultVolume << " Laengeneinheiten" << std::endl;

    std::cout << "QUAD(4-1)=" << QUAD(4 - 1) << std::endl;
    std::cout << "\nOberflaeche: " << 4.0 * M_PI * QUAD(r) << ", Volumen: " << 4.0 / 3 * PI * CUBE(r) << std::endl;
}