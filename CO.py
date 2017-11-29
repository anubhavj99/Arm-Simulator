address = 2;
hexcommand = 1;
flag = "";
immediate = 0;
operandOne = 0;
destination = 0;
operandTwo = 0;
groupCode = 0;
condition = 0;
offset = 0;
offsetValue = 0;
result = 0
N = 0
Z = 0
V = 0
C = 0
opcode = -1;
fileData = [];
MEM = [0 for i in range(4096)];
R = [0 for i in range(16)];
	
import struct
def int32_to_uint32(i):
    return struct.unpack_from("I", struct.pack("i", i))[0]

def fetch():
	global R;
	global address;
	global hexcommand;
	global fileData;
	for i in range(len(fileData)):
		tmpVar = int(fileData[i][0], 16);
		# print(R[15], int(fileData[i][0], 16))
		if tmpVar == R[15]:
			address, hexcommand = fileData[i];
			break;

	print("Fetch instruction 0x", hexcommand, " from address 0x", address, sep="");
	R[15] += 4;

def decode():
	global address;
	global hexcommand;
	global immediate;
	global operandOne;
	global destination;
	global operandTwo;
	global R;
	global opcode;
	global groupCode;
	global condition
	global offset
	hexcommand = int(hexcommand, 16);
	opcode = (hexcommand>>21) & (0xF);
	#print("opcode", opcode);
	global flag;
	flag = (hexcommand>>26) & (0x3);
	# Shifting 26 bits and AND with 11 (3) to get 26th and 27th bit
	#print(flag);
		

	if flag == 0:
		immediate = (hexcommand>>25) & (0x1);
		operandOne = (hexcommand>>16) & (0xF);
		destination = (hexcommand>>12) & (0xF);
		if immediate == 0:
			operandTwo = (hexcommand) & (0xF);
			if opcode == 0:
				print("DECODE: Operation is AND, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 1:
				print("DECODE: Operation is XOR, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 2:
				print("DECODE: Operation is SUB, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 3:
				print("DECODE: Operation is RSB, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 4:
				print("DECODE: Operation is ADD, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 10:
				print("DECODE: Operation is CMP, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 12:
				print("DECODE: Operation is ORR, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 13:
				print("DECODE: Operation is MOV, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 14:
				print("DECODE: Operation is BIC, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 15:
				print("DECODE: Operation is MVN, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");

			print("Read Registers: R", operandOne, " = ", R[operandOne], ", R", operandTwo, " = ", R[operandTwo], sep="");

		else:
			operandTwo = (hexcommand) & (0xFF);
			if opcode == 0:
				print("DECODE: Operation is AND, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 1:
				print("DECODE: Operation is XOR, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 2:
				print("DECODE: Operation is SUB, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 3:
				print("DECODE: Operation is RSB, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 4:
				print("DECODE: Operation is ADD, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 10:
				print("DECODE: Operation is CMP, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 11:
				print("DECODE: Operation is CMN, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 12:
				print("DECODE: Operation is ORR, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 13:
				print("DECODE: Operation is MOV, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 14:
				print("DECODE: Operation is BIC, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 15:
				print("DECODE: Operation is MVN, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");

			print("Read Registers: R", operandOne, " = ", R[operandOne], sep="");
	elif flag == 1:
		groupCode = (hexcommand>>20) & (0x3F);
		operandOne = (hexcommand>>16) & (0xF);
		operandTwo = (hexcommand) & (0xFFF);
		destination = (hexcommand>>12) & (0xF);
		if groupCode == 25:
			print("DECODE: Operation is LDR, Base register is R", operandOne,", Offset is ", operandTwo,", Destination Register is R", destination, sep="");
		elif groupCode == 24:
			print("DECODE: Operation is STR, Base register is R", operandOne,", Offset is ", operandTwo,", Register stored in memory is R", destination, " Read Register: R", destination, " = ", R[destination],sep="");
	elif flag==2:
		condition = (hexcommand>>28) & (0xF);
		offset = (hexcommand) & (0xFFFFFF) ;
		if condition == 0 :
			print("DECODE: Operation is BEQ, offset is : ", hex(offset), sep="");
		elif condition == 1 :
			print("DECODE: Operation is BNE, offset is : ", hex(offset), sep="");
		elif condition == 10 :
			print("DECODE: Operation is BGE, offset is : ", hex(offset), sep="");
		elif condition == 11 :
			print("DECODE: Operation is BLT, offset is : ", hex(offset), sep="");		
		elif condition == 12 :
			print("DECODE: Operation is BGT, offset is : ", hex(offset), sep="");
		elif condition == 13 :
			print("DECODE: Operation is BLE, offset is : ", hex(offset), sep="");
		elif condition == 14:
			print("DECODE: Operation is BAL, offset is : ", hex(offset), sep="");	


def twoComplementToInteger(x):
	a  = bin(x)
	a = str(a)
	a = a[2:];
	negative = False;
	if a[0] == "1" and len(a)==32:
		negative = True;
	for i in range(len(a)):
		if a[i] == "1":
			a = a[:i] + "0" + a[i+1:]
		elif a[i] == "0":
			a = a[:i] + "1" + a[i+1:]
	a = int(a,2)+1;
	# print(a, negative, bin(x));
	if negative:
		a = a * -1;
	return a;


def execute() :
	global address;
	global opcode;
	global hexcommand;
	global immediate;
	global operandOne;
	global destination;
	global operandTwo;
	global R;
	global groupCode;
	global condition
	global offset
	global result
	global N
	global Z
	global V
	global C
	global offsetValue;

	result = 0;
	if flag == 0: 
		carry = (hexcommand>>29) & (0x1) ;
		if immediate == 0 :
			if opcode == 0 : 
				result = R[operandOne] & R[operandTwo]
				print("EXECUTE: AND ", R[operandOne], " and ", R[operandTwo], sep="")
			elif opcode == 1 : 
				result = R[operandOne] ^ R[operandTwo]	
				print("EXECUTE: XOR ", R[operandOne], " and ", R[operandTwo], sep="")
			elif opcode == 2 : 
				result = R[operandOne] - R[operandTwo]	
				print("EXECUTE: SUB ", R[operandOne], " and ", R[operandTwo], sep="")
			elif opcode == 3 : 
				result = R[operandTwo] - R[operandOne]	
				print("EXECUTE: RSB ", R[operandOne], " and ", R[operandTwo], sep="")
			elif opcode == 4 : 
				result = R[operandOne] + R[operandTwo]	
				print("EXECUTE: ADD ", R[operandOne], " and ", R[operandTwo], sep="")	
			elif opcode == 5 : 
				result = R[operandOne] + R[operandTwo] + carry	
				print("EXECUTE: ADC ", R[operandOne], " and ", R[operandTwo], sep="")
			elif opcode == 6 : 
				result = R[operandOne] - R[operandTwo]	+ carry - 1
				print("EXECUTE: SBC ", R[operandOne], " and ", R[operandTwo], sep="")
			elif opcode == 7 : 
				result = R[operandTwo] - R[operandOne]	+ carry - 1
				print("EXECUTE: RSC ", R[operandOne], " and ", R[operandTwo], sep="")	
			# elif opcode == 8 : 
			# 	result = R[operandTwo] - R[operandOne]	+ carry - 1
			# 	print("EXECUTE: TST ", R[operandOne], " and ", R[operandTwo], sep="")
			# elif opcode == 9 : 
			# 	result = R[operandTwo] - R[operandOne]	+ carry - 1
			# 	print("EXECUTE: RSC ", R[operandOne], " and ", R[operandTwo], sep="")
			elif opcode == 10 : 
				print("EXECUTE: CMP ", R[operandOne], " and ", R[operandTwo], sep="")			
				if R[operandOne] == R[operandTwo]: 
					Z = 1
				elif R[operandOne] < R[operandTwo] :
					N = 1
			elif opcode == 12 : 
				result = R[operandOne] | R[operandTwo]
				print("EXECUTE: ORR ", R[operandOne], " and ", R[operandTwo], sep="")	
			elif opcode == 13 : 
				result = R[operandTwo]
				print("EXECUTE: MOV ", R[operandTwo], " in R", destination, sep="")
			elif opcode == 14 : 
				result = R[operandOne] & ~R[operandTwo]
				print("EXECUTE: BIC ", R[operandTwo], " in R", destination, sep="")	
			elif opcode == 15 : 
				result = ~R[operandTwo]
				print("EXECUTE: MVN ", R[operandTwo], " in R", destination, sep="")
		else :
			if opcode == 0 : 
				result = R[operandOne] & R[operandTwo]
				print("EXECUTE: AND ", R[operandOne], " and ", operandTwo, sep="")
			elif opcode == 1 : 
				result = R[operandOne] ^ operandTwo	
				print("EXECUTE: XOR ", R[operandOne], " and ", operandTwo, sep="")
			elif opcode == 2 : 
				result = R[operandOne] - operandTwo	
				print("EXECUTE: SUB ", R[operandOne], " and ", operandTwo, sep="")
			elif opcode == 3 : 
				result = operandTwo - R[operandOne]	
				print("EXECUTE: RSB ", R[operandOne], " and ", operandTwo, sep="")
			elif opcode == 4 : 
				result = R[operandOne] + operandTwo	
				print("EXECUTE: ADD ", R[operandOne], " and ", operandTwo, sep="")	
			elif opcode == 5 : 
				result = R[operandOne] + operandTwo + carry	
				print("EXECUTE: ADC ", R[operandOne], " and ", operandTwo, sep="")
			elif opcode == 6 : 
				result = R[operandOne] - operandTwo	+ carry - 1
				print("EXECUTE: SBC ", R[operandOne], " and ", operandTwo, sep="")
			elif opcode == 7 : 
				result = operandTwo - R[operandOne]	+ carry - 1
				print("EXECUTE: RSC ", R[operandOne], " and ", operandTwo, sep="")	
			# elif opcode == 8 : 
			# 	result = operandTwo - R[operandOne]	+ carry - 1
			# 	print("EXECUTE: TST ", R[operandOne], " and ", operandTwo, sep="")
			# elif opcode == 9 : 
			# 	result = operandTwo - R[operandOne]	+ carry - 1
			# 	print("EXECUTE: RSC ", R[operandOne], " and ", operandTwo, sep="")
			elif opcode == 10 : 
				print("EXECUTE: CMP ", R[operandOne], " and ", operandTwo, sep="")			
				if R[operandOne] == operandTwo: 
					Z = 1
					N = 0
				elif R[operandOne] < operandTwo :
					N = 1
					Z = 0
				elif R[operandOne] > operandTwo :
					N = 0
					Z = 0
			elif opcode == 12 : 
				result = R[operandOne] | operandTwo
				print("EXECUTE: ORR ", R[operandOne], " and ", operandTwo, sep="")	
			elif opcode == 13 : 
				result = operandTwo
				print("EXECUTE: MOV ", operandTwo, " in R", destination, sep="")
			elif opcode == 14 : 
				result = R[operandOne] & ~operandTwo
				print("EXECUTE: BIC ", operandTwo, " in R", destination, sep="")	
			elif opcode == 15 : 
				result = ~operandTwo
				print("EXECUTE: MVN ", operandTwo, " in R", destination, sep="")
	elif flag == 1:
		offsetValue = int(operandTwo/4);
		print("EXECUTE: Address calculated to be", hex(offsetValue));
	elif flag == 2:
		operandOne = 0;
		if condition == 0 :
			if Z == 1 and N == 0:
				operandOne = 1;
		elif condition == 1 :
			if Z == 0:
				operandOne = 1;
		elif condition == 10 :
			if N == 0 or Z == 1:
				operandOne = 1;
		elif condition == 11 :
			if N == 1 and Z == 0:
				operandOne = 1;
		elif condition == 12 :
			if N == 0 and Z == 0:
				operandOne = 1;
		elif condition == 13 :
			if N == 1 or Z == 1 :
				operandOne = 1;
		elif condition == 14:
			operandOne = 1;

		if operandOne == 1:
			tmp = ((offset) & (0x800000))<<1;
			for i in range(8):
				offset += tmp;
				tmp = tmp << 1;
			# print(offset, bin(offset))
			offset = twoComplementToInteger(offset);
			offset = offset << 2;
			# print(offset, R[15])
			R[15] += offset + 4;
			print("EXECUTE: Updating PC to ", hex(R[15]), sep="");
		else:
			print("EXECUTE: No execution", hex(R[15]));


def memory() :
	global address;
	global opcode;
	global hexcommand;
	global immediate;
	global operandOne;
	global destination;
	global operandTwo;
	global offsetValue;
	global R;
	global groupCode;
	global condition
	global offset
	global result
	global N
	global Z
	global V
	global C

	if flag==1 :
		if groupCode == 24 :
			BaseAddress = R[operandOne] + offsetValue;
			MEM[BaseAddress] = R[destination]
			print("MEMORY : Store in Memory", BaseAddress)
		elif groupCode == 25 :
			BaseAddress = R[operandOne] + offsetValue
			Value = MEM[BaseAddress]
			result = Value
			# print("MEMORY : Load from Memory", BaseAddress)
	elif flag == 0 or flag == 2 :
		print("MEMORY : No memory operation")		

def writeBack():
	global address;
	global opcode;
	global hexcommand;
	global immediate;
	global operandOne;
	global destination;
	global operandTwo;
	global R;
	global groupCode;
	global condition
	global offset
	global result
	global N
	global Z
	global V
	global C

	if flag == 0 :
		if opcode == 10 :
			print("WRITEBACK: No writeBack Operation")
		else : 
			R[destination] = result
			print("WRITEBACK: Write ", result, " to R", destination, sep="")
	elif flag == 1 :
		if groupCode == 24 :
			print("WRITEBACK: No writeBack Operation")
		elif groupCode == 25 :
			print("WRITEBACK: Write ", result, " to R", destination, sep="")
	elif flag == 2 :
		print("WRITEBACK: No writeBack Operation", hex(R[15]))	

	elif flag == 3 : 
		print("EXIT");
		import sys
		sys.exit();					



if __name__ == '__main__':
	file = open("input.mem", "r");
	fileData = file.readlines();
	file.close();
	for i in range(len(fileData)):
		fileData[i] = fileData[i].replace("\n", "");
		fileData[i] = fileData[i].replace("0x", "");
		fileData[i] = fileData[i].split(" ");
		fileData[i][0] = fileData[i][0];
	print(fileData, "\n");
	while True:
		fetch();
		decode();
		execute();
		memory();
		writeBack();
		# print(R);
		# print(N,Z);
		print();






