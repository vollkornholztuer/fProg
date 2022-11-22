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


template <int Bits>
class BitSet
{
	// Bits must be divisible by 2
	static_assert(Bits%2==0, "Only even count bit size is supported.");

	// Class definition here...
};




void StaticAssertExamples()
{
	const int nErrorCode = 100;

	// The following compiler error is expected
	// Just set nErrorCode above to 100
	static_assert(nErrorCode == 100, "Expected error - Error code must be set to 100");


	// Check if being compiled as 32-bit or not...
	static_assert(sizeof(void *) == 4, "This code should only be compiled as 32-bit.");



	// Generate other errors yourself!
	BitSet<4> FourBits;
	
	FourBits;	// Just to avoid warning

	// BitSet class doesn't support odd-size bits
	// uncomment following line to get error

	//# BitSet<3> ThreeBits;


	// This is NOT possible with static_assert keyword, since it checks at runtime
	int nValue = 2;

	//# static_assert(nValue>10, "Value must be more than 10");
}