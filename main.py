import re
import sys

program = []
machineCode = []

tmp = ""
outputMode = ""
outputMode = input("Type 'h' to have the output written in hex, or 'b' to have the output in binary: ")
if outputMode != 'h' and outputMode != 'b':
    print("Unrecognised output mode")
    sys.exit()

while tmp != "exit":
    tmp = input(">")
    if tmp != "exit":
        program.append(tmp)

inputMap = {"Ra": "00", "Rb": "01", "Rc": "10", "Rd": "11", "MOV": "000", "ADD": "001", "SUB": "010", "ADC": "011",
            "LDR": "100", "STR": "101", "JMP": "1100", "JNE": "1101", "JCS": "1110", "JMI": "1111"}

for i in range(len(program)):
    tmp_li = re.split(" ", program[i])
    instruction = inputMap.get(tmp_li[0])
    if tmp_li[0] == "MOV" or tmp_li[0] == "ADD" or tmp_li[0] == "SUB" or tmp_li[0] == "ADC":
        if tmp_li[2][0] == "R":
            instruction += "0"
            instruction += inputMap.get(tmp_li[1])
            instruction += inputMap.get(tmp_li[2])
            instruction += "00000000"
        else:
            instruction += "1"
            instruction += inputMap.get(tmp_li[1])
            instruction += "00"
            instruction += "{0:08b}".format(int(tmp_li[2], 16))
            # print(instruction)

    elif tmp_li[0] == "LDR" or tmp_li[0] == "STR":
        instruction += "0"
        instruction += inputMap.get(tmp_li[1])
        instruction += "00"
        instruction += "{0:08b}".format(int(tmp_li[2], 16))

    elif tmp_li[0] == "JMP" or tmp_li[0] == "JNE" or tmp_li[0] == "JCS" or tmp_li[0] == "JMI":
        instruction += "0000"
        instruction += "{0:08b}".format(int(tmp_li[1], 16))
    else:
        print("Error on line " + i + ", invalid operation")
        sys.exit()
    machineCode.append(instruction)

for i in range(len(program)):
    if outputMode == "b":
        print(machineCode[i])
    else:
        tmp = int(machineCode[i], 2)
        print("0x" + format(tmp, 'x'))
