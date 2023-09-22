
==================== PROJECT DETAILS ====================

< Project Folder (Pre-Fix) Path: doxygen_projects/chrone_2

=========================================================

>> FILE: classepre.h
>> FILE CONTENT (Pre-Fix):

#pragma once

class Serial : public IMemoryUnit
{
public:


    Serial();


    ~Serial();


    byte ReadByte(const ushort& address);


    bool WriteByte(const ushort& address, const byte val);

private:
    byte m_Data;
};

---------------------------------------------------------



>> Number of Doxygen Warnings Detected (Pre-Fix): 3

>> Warning Contents (Pre-Fix):

	>>> Warning 1: warning: Compound Serial is not documented.
	>>> On Line: 3

	>>> Warning 2: warning: Member ReadByte(const ushort &address) (function) of class Serial is not documented.
	>>> On Line: 14

	>>> Warning 3: warning: Member WriteByte(const ushort &address, const byte val) (function) of class Serial is not documented.
	>>> On Line: 17

---------------------------------------------------------

2023-09-22 19:44:48 - File analysis completed.
=========================================================

