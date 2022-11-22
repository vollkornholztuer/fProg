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



#include "stdafx.h"

void Take(void*);
void Take(int);

void NullPtrExamples()
{
	// Since this project/source-code is NATIVE only
	// nullptr and Microsoft specific __nullptr would mean the same.

	// Assigns null pointer
	int* pAllocation = nullptr;


	pAllocation = new int[100];

	// Can check like:
	if (pAllocation != nullptr)
	{
		std::cout << "Allocated successfully"<<std::endl;
	}


	// Would call (void*) version
	Take(pAllocation);
	Take(nullptr);


	// Would call (int) version
	Take(0);
	Take(10);


	// IMPORTANT!
	// Would call (int) version, since NULL is just defined as: 
		// #define NULL 0
	// In C, however, it is defined as
	   // #define NULL    ((void *)0)
	   // It doesn't matter, since C doesn't have function overloading.

	Take(NULL);		// Calls (int) version


	// __nullptr is equivalent to nullptr
	// This keyword is ONLY meaningful for C++/CLI (Managed C++)
	// compilation; to explicitly specify native-null-pointer
	// Even in CLI, 'nullptr' may be used to specify managed or native
	// null pointer. 
	// See MSDN for more details. 
	
	Take(__nullptr);	


	delete []pAllocation;

	// Reset
	pAllocation = nullptr;

}

void Take(void*)
{
	std::cout<<"Pointer version"<<std::endl;
}

void Take(int)
{
	std::cout<<"Integer version"<<std::endl;
}