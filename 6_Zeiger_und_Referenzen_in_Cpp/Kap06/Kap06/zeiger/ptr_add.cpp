/* Datei: ptr_add.cpp */
#include <iostream>

using namespace std;

void einstieg()
{
    int* p1;
    double * p2;
    char **p3;

    int i = 17;
    p1 = &i;
    cout << "Adresse: " << p1 << ", Inhalt: " << *p1 << endl;

    //Was wird hier deklariert?
    int* q1, q2;
}

int alpha ()
{
   int alpha [6] = {3,5,7,11,13,17};
   int* pointer;
   int lv = 0;

   pointer = alpha;
   cout << "Groesse alpha: " << sizeof(alpha)
       << ", Groesse pointer: " << sizeof(pointer) << endl << endl;

   while (lv < 6)
   {
        cout << *pointer << " " << pointer << endl;
        pointer++;
        lv++;
   }

   for (pointer = alpha, lv = 0; lv < 6; pointer++, lv++)
       cout << *pointer << " "; 

   cout << endl;
   return 0;
}

int main()
{
    einstieg();

    // alpha();

    return 0;
}