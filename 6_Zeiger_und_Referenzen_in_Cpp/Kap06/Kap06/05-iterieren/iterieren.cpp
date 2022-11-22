/* cppbuch/k4/carrayIterieren.cpp
   Beispiel zum Buch von U. Breymann: Der C++ Programmierer; 4. Aufl. Hanser 2015
   Diese Software ist freie Software. Website: http://www.cppbuch.de/
*/
#include <iostream>
#include <vector>
#include <iterator> // begin() und end()

int main() {
	int carray[]{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	
	for (int i : carray)
	{
		std::cout << i << " ";
	}
	std::cout << std::endl;

	for (int i : carray)
	{
		std::cout << ++i << " ";
	}
	std::cout << std::endl;

	for (auto i : carray)
	{
		std::cout << i << " ";
	}
	std::cout << std::endl;

	//for (int& i : carray)
	//{
	//	std::cout << ++i << " ";
	//}
	//std::cout << std::endl;

	// Version mit begin und end
	auto anfang = std::begin(carray);

	while (anfang != std::end(carray)) {
		std::cout << *anfang++ << ' ';
	}
	std::cout << std::endl;

}
