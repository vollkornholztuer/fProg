/* Fortgeschrittene Programmierung
   HS Coburg
   
   Hinweis zum Testen: Am besten mit zyklischen Matrizen wie z.B.

         (1 2 3)
     A = (2 3 1)
	     (3 1 2)

   Den Betrag der Determinante kann man berechnen über die Formel:
     |det(A)| = (n+1)/2 * n^{n-1}, für A3 heißt das:
	 |det(A3)|= 4/2 * 3^2 = 2 * 9 = 18
*/

#include <iostream>

using namespace std;

double determinante(double** a, int n);

int main(void)
{
    double**    a;
    int         i, j, n;
    
    cout << "Berechnung der Determinante einer quadratischen Matrix" << endl << endl;

    // Eingabe der Dimension
    cout << "Anzahl der Zeilen und Spalten: ";
    cin >> n;
    if (n <= 0)
    {
        cerr << "Ungültige Dimension!" << endl;
        return -1;
    }
    
    // Speicherplatzreservierung 
    a = new double*[n];
    for(i = 0; i < n; i++)
        a[i] = new double[n];
        
    // Eingabe der Matrixelemente 
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
        {
            cout << "a[" << i + 1 << "][" << j + 1 << "] = ";
            cin >> a[i][j];
        }
      
    // Berechung und Ausgabe des Ergebnisses 
    cout << endl << "Die Determinante dieser Matrix ist " 
		 << determinante(a, n);
        
    // Freigabe des Speichers 
	for(i = 0; i < n; i++)
        delete[] a[i];
    delete[] a;

    return 0;
}

double determinante(double** a, int n)
{
    int sig = 1;
    int i, j, k, l;
    double** a_unter;
    double det = 0.0;
    
    if (n == 1)
        return a[0][0];
        
    if (n == 2)
        return (a[0][0] * a[1][1] - a[0][1] * a[1][0]);
        
    // Speicherplatzreservierung für Untermatrix 
	a_unter = new double*[n-1];
    for(i = 0; i < n - 1; i++)
		a_unter[i] = new double[n-1];
        
    // Entwicklung der Determinante nach der ersten Zeile 
    for(k = 0; k < n; k++, sig *= -1)
    {
        // Erstellung der Untermatrix 
        for(i = 1; i < n; i++)
            for (j = l = 0; j < n; j++)
                if (j != k)
                    a_unter[i - 1][l++] = a[i][j];
                    
        // Rekursiver Aufruf 
        det += a[0][k] * sig * determinante (a_unter, n - 1);
    }
    
    // Freigabe des Speichers für die Untermatrix 
    for(i = 0; i < n - 1; i++)
        delete[] a_unter[i];
    delete[] a_unter;
     
    return det;
}

