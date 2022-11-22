// Copyright (C) 
// Ajay Vijayvargiya

// This source code was published on CodeProject.com, under CPOL license
// This code CANNOT be used for similar publication on the web or as printed material.
// This can, however, be used as educational reference in educational institutions.
// You are allowed to use the accompanying code in your programs, 
//    commercial or non commercial. 

// This source code is only intended to explain the new C++ standard (codenamed as C++0x),
// and thus may contain bugs, some logical issues etc.
// The explanation is relevant to Visual C++ 2010 (Compiler version: 16.0)

// http://www.codeproject.com/KB/cpp/cpp10.aspx 

// Code that is invalid/errornous is marked as //#


#include"stdafx.h"


void AutoWithStruct();
void AutoWithSTL();

constexpr int factorial(int n)
{
	return (n == 1) ? 1 : n * factorial(n - 1);
}

void AutoKeywordExamples()
{
	// deduce int
	auto nVariable1 = 56 + 54;

	// int
	auto nVariable2 = 100 / 3; 

	// double
	auto nVariable3 = 100 / 3.0;

	// long, since labs returns long
	auto nVariable4 = labs(-127);


	// Calls sqrt with 'double', and that overloaded returns double
	// Thus deduced as double
	auto nVariable5 = sqrt(nVariable3);

	// nVariable4 is long, sqrt doesn't have (long) overloaded
	// Thus, following results in compiler error.
	auto nVariable = sqrt(nVariable4);

	// Deduced as int*	
	auto pVariable6 = &nVariable1;

	// Again, Deduced as int*
	auto* pVariable7 = &nVariable1;

	// Deduced as int**
	auto* pVariable8 = &pVariable7;

	// int &
	auto & rVariable9 = nVariable1;


	// Cannot have array declared with auto
	//# auto aArray1[10];
	//# auto aArray[]={1,2,3,4,5};


	// Cannot mix multiple types in same declaration statement
	//# auto a=10, b=10.30, s="new";

	// Cannot mix, both functions returns different types!
	//# auto nVariable = sqrt(100.0), nVariableX = labs(100);


	// Constant declarations
	const auto PI = 3.14;
	const auto SqRoot2 = sqrt(2.0);

	// Would be size_t (or may be int...)
	const auto nStringLen = strlen("CodeProject.com"); 

	// 32-bit or 64-bit (See time function)
	const auto nTime = time(0);

	// Volatile
	volatile auto IsFinished = false;  // bool

	// See below
	AutoWithStruct();

	// With STL
	AutoWithSTL();

	std::cout << "Fakultaet: " << factorial(10) << std::endl;
	// Other source files uses 'auto' also.
}



// Cannot be return type
//# auto ReturnDeduction(); 

// cannot be argument
//# void ArgumentDeduction(auto x);

struct AutoStruct 
{
	// Cannot declare with auto, which is also not allowed in old C++
    //# auto Variable = 10; 

	// Only static constant integer is allowed here!	
	static const auto nVariable = 50;

	~AutoStruct()
	{

	}
};

AutoStruct GetStruct()
{
	return AutoStruct();
}

AutoStruct* GetNewStruct()
{
	return new AutoStruct;
}

void AutoWithStruct()
{
	// AutoStruct deduction
	auto s = GetStruct();

	// Possible, AutoStruct* deduction
	// Invalid!
	//auto* sp=  &GetStruct();

	// Unfortunately BOTH are same!
	// Both deduces to AutoStruct*
	auto* sp1 = GetNewStruct();
	auto sp2 = GetNewStruct();


	// Calls AutoStruct::~AutoStruct
	delete sp1;
	delete sp2;
}



void AutoWithSTL()
{
	// This code section assumes that you know basics of templates and STL, and what
	// iterators are.

	using namespace std;

	vector<int> IntVector;

	IntVector.push_back(20);
	IntVector.push_back(60);
	IntVector.push_back(75);
	IntVector.push_back(100);
	IntVector.push_back(512);

	// Display numbers with looping over the vector
	// OLD style, cumbersome!
	for(vector<int>::const_iterator iter = IntVector.begin();
		iter != IntVector.end();   ++iter)
	{
		cout << (*iter) << endl;
	}

	// New Style!
	for(auto iter = IntVector.begin();	iter != IntVector.end();   ++iter)
	{
		cout << (*iter) << endl;


		// Since vector::begin returns iterator (NOT const_iterator)
		// Modifying is allowed (adding 10)
		(*iter) += 10;
	}

	// Proper way to iterate through (i.e. const_iterator usage)
	// See 'cbegin' and 'cend' usage
	for(auto iter = IntVector.cbegin();	iter != IntVector.cend();   ++iter)
	{
		cout << (*iter) << endl;


		// Now following will not compile, since iter is const_iterator
		//# (*iter) += 10;
	}
	
	// With map!
	map<vector<int>, string> StringMap;

	// Old style
	map<vector<int>, string>::const_iterator m_iter = StringMap.begin();

	// Better style
	auto m_iter1 = StringMap.cbegin();
}