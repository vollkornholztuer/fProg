#include <iostream>
#include <algorithm>

#define SIZE 5
#define SWAP(X, Y)        \
    {                     \
        int t = (X);      \
        (X) = (Y)(Y) = t; \
    }

// "&" - Heißt: Referenz wird übergeben (Speicherstelle)
inline void swap(int &x, int &y)
{
    int t = x;
    x = y;
    y = t;
}

int main()
{
    int numbers[SIZE];
    std::cout << "Geben sie 5 ganzzahlen ein" << std::endl;
    for (int i = 0; i < SIZE; i++)
    {
        std::cout << "Geben Sie die " << i + 1 << ". Zahl ein:" << std::endl;
        std::cin >> numbers[i];
    }

    int numbersArrayLength = sizeof(numbers) / sizeof(int); // Arraylänge berechnen

    // Bubblesort
    bool swapped = true;
    while (swapped)
    {
        swapped = false;
        for (int i = 1; i < numbersArrayLength; i++)
        {
            if (numbers[i - 1] > numbers[i])
            {
                swapped = true;
                int temp = numbers[i - 1];
                numbers[i - 1] = numbers[i];
                numbers[i] = temp;
            }
        }
    }

    // Print Array
    std::cout << "[";
    for (int i = 0; i < numbersArrayLength; i++)
    {
        std::cout << numbers[i] << ", ";
    }
    std::cout << "]" << std::endl;

    int median = numbers[numbersArrayLength / 2];

    std::cout << "Der Median vom Array ist: " << median << std::endl;
}