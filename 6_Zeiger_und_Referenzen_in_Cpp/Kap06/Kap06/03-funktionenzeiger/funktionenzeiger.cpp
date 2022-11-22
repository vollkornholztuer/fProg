#include <iostream>
#include <cmath>

using namespace std;

#define PI (float)(4.0f*atan(1))

float berechne( float rad, float (*welche_funktion)(float rad) )
{
    return(welche_funktion(rad));
}

/* Alternative Deklaration mit typedef */
typedef float (*Berechnungsfunktion) (float);

typedef unsigned int UINT;

float berechne2( float rad, Berechnungsfunktion welche_funktion)
{
    return((*welche_funktion)(rad));
}

/* auszuwählende Funktionen */
float zyl_vol(float r) { return(r*r*PI); }

float kug_vol(float r) { return(r*r*r*4.0f/3.0f*PI); }

/* main-Block */
int main(void)
{
    float radius, hoehe;
    char wahl;
    cout << "\nVolumen eines Zylinders oder einer Kugel ( Z/K ) ? ";
    cin >> wahl;
    wahl = toupper(wahl);
    
    cout << "\nGeben Sie Radius ein: ";
    cin >> radius; 
    if (wahl=='Z') {
        cout << "Geben Sie Hoehe des Zylinders ein: "; 
        cin >> hoehe; 
        cout << " ---> Volumen (Zylinder): " << hoehe*berechne(radius,zyl_vol) << endl;
    } 
    else
        cout << " ---> Volumen (Kugel): " << berechne(radius,kug_vol) << endl;
        
	return 0;
}
