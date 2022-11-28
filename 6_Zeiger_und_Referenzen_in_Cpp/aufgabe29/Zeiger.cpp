// Kapitel 6, Aufgabe 29

#include <iostream>

int main()
{
    // a ist ein Zeiger auf einen konstanten float-Wert.
    float x = 1.0f;
    float *a = &x; // &x = Adresse von x
    *a = 0.0;

    // b ist ein konstanter Zeiger auf eine float-Variable
    float const *b; // oder float const * b = NULL;

    // c ist ein Zeiger auf einen konstanten Zeiger auf eine float-Variable
    float *const *c;

    // d ist ein Array mit 3 Zeigern auf float-Variablen
    float *d[3];

    // e ist ein Zeiger auf ein Array mit 3 Zeigern auf float-Variablen.
    float *(*e)[3];
}