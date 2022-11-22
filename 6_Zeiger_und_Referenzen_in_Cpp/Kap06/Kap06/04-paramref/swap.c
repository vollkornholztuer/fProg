#include <stdio.h>

// call by reference
void swap(int *a, int* b)
{
	int t = *a;
	//a = NULL;
	*a = *b;
	*b = t;
}

// call by value
void swap2(int a, int b)
{
	int t = a;
	a = b;
	b = t;
}

void swap3(int* a, int* b)
{
	int* t = a;
	a = b;
	b = t;
}

int main()
{
	int a = 7;
	int b = 12;

	printf("a = %d, b = %d\n", a, b);

	swap(&a, &b);
	printf("a = %d, b = %d\n", a, b);

	swap2(a, b);
	printf("a = %d, b = %d\n", a, b);

	swap3(&a, &b);
	printf("a = %d, b = %d\n", a, b);
	
	return 0;
}