/* Datei: ptrarith.cpp */
/* Programm zur Zerlegung einer short int-Zahl in das             */
/* niederwertige und das h�herwertige Byte                        */
#include <iostream>

using namespace std;

int main()
{
   short int zahl, *pointer1; /* pointer1 ist ein Pointer        */
                              /* auf short int                   */
   unsigned char *pointer2;   /* pointer2 ist ein Pointer        */
                              /* auf unsigned char               */

   zahl = 0x7FED; /* Wertzuweisung an Variable zahl  */
   cout << "Zahl ist " << hex << zahl << endl;

   pointer1 = &zahl; /* pointer1 auf                    */
                     /* short int-Variable zahl setzen  */
   cout << endl
        << "pointer1 zeigt auf die Adresse: " << pointer1 << endl;
   cout << "Der Inhalt an der Adresse pointer1 ist: " << *pointer1 << endl;

   /* Pointertyp-Konvertierung                                    */
   pointer2 = (unsigned char *)pointer1;

   pointer1 += 1;
   cout << endl
        << "pointer1 zeigt auf die Adresse: " << pointer1 << endl;

   /* Ausgabe des niederwertigen Bytes                            */
   cout << "Ausgabe des niederwertigen Bytes:" << endl;
   cout << "pointer2 zeigt auf die Adresse: " << (int *)pointer2 << endl;
   cout << "Der Inhalt an der Adresse pointer2 ist: " << (int)*pointer2 << endl;

   pointer2 += 1; /* pointer2 wird um 1 erhoeht      */
   cout << endl
        << "pointer2 wurde um 1 erhoeht" << endl;

   /* Ausgabe des hoeherwertigen Bytes                            */
   cout << "Ausgabe des hoeherwertigen Bytes:" << endl;
   cout << "pointer2 zeigt jetzt auf die Adresse: " << (int *)pointer2 << endl;
   cout << "Der neue Inhalt an der Adresse pointer2 ist: " << (int)*pointer2 << endl;

   return 0;
}
