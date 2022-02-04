# EEP0-Assembly-To-Machine-Code
This python script allows you to enter a program for the EEP0 cpu in assembly code, and get the ouput in machine code

Example:

Type 'h' to have the output written in hex, or 'b' to have the output in binary: 

INPUT:

h

MOV R0 0x44

ADD R1 0x12

SUB R0 R1

JMP 0x00

exit

OUPUT:

0x1044

0x3412

0x4100

0xC000
