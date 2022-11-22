//
// paramref.cpp
// Beispielprogramm fuer Parameteruebergabe als Referenz
//

#include <iostream>

using namespace std;

void swap_values (int x, int y)
{
  int temp = x;
  x = y;
  y = temp;
  return;
}

void swap_refs (int& x, int& y)
{
  int temp = x;
  x = y;
  y = temp;
  return;
}

void swap_ptr(int* a, int* b)
{
	int temp = *a;
	//a = NULL;
	*a = *b;
	*b = temp;
}

int main (void)
{
  int big = 11;
  int small = 22; 

  cout << "big1: "<< big << " small1: "<< small << endl;
  
  swap_values (big, small);
  cout << "big2: "<< big << " small2: "<< small << endl;
  
  swap_refs (11, 22);
  cout << "big3: "<< big << " small3: "<< small << endl;

  std::swap(big, small);
  cout << "big4: " << big << " small4: " << small << endl;

  swap_ptr(&big, &small);
  cout << "big5: " << big << " small5: " << small << endl;

  return 0;
}

