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


// This source file assumes that you have understood 'auto' keyword
// as explicated in Auto.cpp


#include"stdafx.h"


void DeclTypeExamples()
{
	// Declaring variable of underlying type of M_PI
	decltype(M_PI) Radius;

	// Radius variable would be double
	Radius = 10.477;

	auto nSqrt = sqrt(256.0);

	// Type deduction from another variable
	// It results in double. Just change sqrt above,
	// like sqrt((float)256), THIS variable would have that type!
	decltype(nSqrt) nCubeRoot = 10;
	size_t
	// Directly deduce form function's return type
	// Remember that function labs will NOT BE called
	// This is just expression for the compiler
//	decltype(labs(0)) nAbsolute;
	nAbsolute=0;

	// This is perfectly valid!
	decltype(1/0) Infinite; // No compiler error for "divide by zero" !
	Infinite=0;



	// ----- FEW STL EXAMPLES ----
	using namespace std;

	vector<string> Strings;

	// Type of iterator would be: vector<string>::const_iterator
	decltype(Strings.cbegin()) iter;

	// Just for example...
	iter = Strings.cend();

	map<int,string> IntStrMap;

	// Hold the underlying allocator type of 'second' 
	decltype(IntStrMap.begin()->second.get_allocator()) under_alloc;
}