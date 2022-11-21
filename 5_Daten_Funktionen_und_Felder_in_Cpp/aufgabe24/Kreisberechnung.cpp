#include <iostream>
#include <math.h>

int main()
{
    float radius = 0;
    float pi = 3.1415927;

    std::cout << "Dieses Programm berechnet die Oberfläche und das Volumen eines Kreises" << std::endl;
    std::cout << "Geben Sie ein Radius ein" << std::endl;
    std::cin >> radius;

    float resultArea = 4 * pi * pow(radius, 2);
    float resultVolume = (4 / 3) * pi * pow(radius, 3);

    std::cout << "Oberflaeche der Kugel: " << resultArea << " Laengeneinheiten" << std::endl;
    std::cout << "Volumen der Kugel: " << resultVolume << " Laengeneinheiten" << std::endl;
}