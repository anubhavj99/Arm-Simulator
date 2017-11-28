file = "";
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
result = 0
N = 0
Z = 0
V = 0
C = 0
opcode = -1;

R = [[0 for j in range(256)] for i in range(16)];
PC = 0;

def fetch():
	global file;
	global PC;
	r = file.read(15);
	global address;
	global hexcommand;
	r = r.replace("\n", "");
	address, hexcommand = r.split(" ");
	print("Fetch instruction "+hexcommand+" from address "+address)
	PC += 4;

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

	address = address[2:];
	hexcommand = hexcommand[2:];
	hexcommand = (int(hexcommand, 16));
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
			elif opcode == 5:
				print("DECODE: Operation is ADC, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 6:
				print("DECODE: Operation is SBC, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 7:
				print("DECODE: Operation is RSC, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 8:
				print("DECODE: Operation is TST, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 9:
				print("DECODE: Operation is TEQ, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 10:
				print("DECODE: Operation is CMP, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 11:
				print("DECODE: Operation is CMN, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 12:
				print("DECODE: Operation is ORR, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 13:
				print("DECODE: Operation is MOV, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 14:
				print("DECODE: Operation is BIC, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 15:
				print("DECODE: Operation is MVN, First Operand is R", operandOne,", Second Operand is R", operandTwo,", Destination Register is R", destination, sep="");

			print("Read Registers: R", operandOne, " = ", R[operandOne][0], ", R", operandTwo, " = ", R[operandTwo][0], sep="");

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
			elif opcode == 5:
				print("DECODE: Operation is ADC, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 6:
				print("DECODE: Operation is SBC, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 7:
				print("DECODE: Operation is RSC, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 8:
				print("DECODE: Operation is TST, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
			elif opcode == 9:
				print("DECODE: Operation is TEQ, First Operand is R", operandOne,", immediate second Operand is ", operandTwo,", Destination Register is R", destination, sep="");
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

			print("Read Registers: R", operandOne, " = ", R[operandOne][0], sep="");
	elif flag == 1:
		groupCode = (hexcommand>>20) & (0x3F);
		operandOne = (hexcommand>>16) & (0xF);
		operandTwo = (hexcommand) & (0xFFF);
		destination = (hexcommand>>12) & (0xF);
		if groupCode == 25:
			print("DECODE: Operation is LDR, Base register is R", operandOne,", Offset is ", operandTwo,", Destination Register is R", destination, sep="");
		elif groupCode == 24:
			print("DECODE: Operation is STR, Base register is R", operandOne,", Offset is ", operandTwo,", Register stored in memory is R", destination, " Read Register: R", destination, " = ", R[destination][0],sep="");
	elif flag==2:
		condition = (hexcommand>>28) & (0xF);
		offset = (hexcommand) & (0xFFFFFF) ; 
		if condition == 0 :
			print("DECODE: Operation is BEQ, offset is : ", offset, sep="");
		elif condition == 1 :
			print("DECODE: Operation is BNE, offset is : ", offset, sep="");
		elif condition == 10 :
			print("DECODE: Operation is BGE, offset is : ", offset, sep="");
		elif condition == 11 :
			print("DECODE: Operation is BLT, offset is : ", offset, sep="");		
		elif condition == 12 :
			print("DECODE: Operation is BGT, offset is : ", offset, sep="");
		elif condition == 13 :
			print("DECODE: Operation is BLE, offset is : ", offset, sep="");
		elif condition == 14:
			print("DECODE: Operation is BAL, offset is : ", offset, sep="");	
	
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

	N = 0
	Z = 0
	V = 0
	Z = 0

	result = 0;
	if flag == 0: 
		carry = (hexcommand>>29) & (0x1) ;
		if immediate == 0 :
			if opcode == 0 : 
				result = R[operandOne][0] & R[operandTwo][0]
				print("EXECUTE: AND ", R[operandOne][0], " and ", R[operandTwo][0], sep="")
			elif opcode == 1 : 
				result = R[operandOne][0] ^ R[operandTwo][0]	
				print("EXECUTE: XOR ", R[operandOne][0], " and ", R[operandTwo][0], sep="")
			elif opcode == 2 : 
				result = R[operandOne][0] - R[operandTwo][0]	
				print("EXECUTE: SUB ", R[operandOne][0], " and ", R[operandTwo][0], sep="")
			elif opcode == 3 : 
				result = R[operandTwo][0] - R[operandOne][0]	
				print("EXECUTE: RSB ", R[operandOne][0], " and ", R[operandTwo][0], sep="")
			elif opcode == 4 : 
				result = R[operandOne][0] + R[operandTwo][0]	
				print("EXECUTE: ADD ", R[operandOne][0], " and ", R[operandTwo][0], sep="")	
			elif opcode == 5 : 
				result = R[operandOne][0] + R[operandTwo][0] + carry	
				print("EXECUTE: ADC ", R[operandOne][0], " and ", R[operandTwo][0], sep="")
			elif opcode == 6 : 
				result = R[operandOne][0] - R[operandTwo][0]	+ carry - 1
				print("EXECUTE: SBC ", R[operandOne][0], " and ", R[operandTwo][0], sep="")
			elif opcode == 7 : 
				result = R[operandTwo][0] - R[operandOne][0]	+ carry - 1
				print("EXECUTE: RSC ", R[operandOne][0], " and ", R[operandTwo][0], sep="")	
			# elif opcode == 8 : 
			# 	result = R[operandTwo][0] - R[operandOne][0]	+ carry - 1
			# 	print("EXECUTE: TST ", R[operandOne][0], " and ", R[operandTwo][0], sep="")
			# elif opcode == 9 : 
			# 	result = R[operandTwo][0] - R[operandOne][0]	+ carry - 1
			# 	print("EXECUTE: RSC ", R[operandOne][0], " and ", R[operandTwo][0], sep="")
			elif opcode == 10 : 
				print("EXECUTE: CMP ", R[operandOne][0], " and ", R[operandTwo][0], sep="")			
				if R[operandOne][0] == R[operandTwo][0]: 
					Z = 1
				elif R[operandOne][0] < R[operandTwo][0] :
					N = 1
			elif opcode == 12 : 
				result = R[operandOne][0] | R[operandTwo][0]
				print("EXECUTE: ORR ", R[operandOne][0], " and ", R[operandTwo][0], sep="")	
			elif opcode == 13 : 
				result = R[operandTwo][0]
				print("EXECUTE: MOV ", R[operandTwo][0], " in R", destination, sep="")
			elif opcode == 14 : 
				result = R[operandOne][0] & ~R[operandTwo][0]
				print("EXECUTE: BIC ", R[operandTwo][0], " in R", destination, sep="")	
			elif opcode == 15 : 
				result = ~R[operandTwo][0]
				print("EXECUTE: MVN ", R[operandTwo][0], " in R", destination, sep="")
		else :
			if opcode == 0 : 
				result = R[operandOne][0] & R[operandTwo][0]
				print("EXECUTE: AND ", R[operandOne][0], " and ", operandTwo, sep="")
			elif opcode == 1 : 
				result = R[operandOne][0] ^ operandTwo	
				print("EXECUTE: XOR ", R[operandOne][0], " and ", operandTwo, sep="")
			elif opcode == 2 : 
				result = R[operandOne][0] - operandTwo	
				print("EXECUTE: SUB ", R[operandOne][0], " and ", operandTwo, sep="")
			elif opcode == 3 : 
				result = operandTwo - R[operandOne][0]	
				print("EXECUTE: RSB ", R[operandOne][0], " and ", operandTwo, sep="")
			elif opcode == 4 : 
				result = R[operandOne][0] + operandTwo	
				print("EXECUTE: ADD ", R[operandOne][0], " and ", operandTwo, sep="")	
			elif opcode == 5 : 
				result = R[operandOne][0] + operandTwo + carry	
				print("EXECUTE: ADC ", R[operandOne][0], " and ", operandTwo, sep="")
			elif opcode == 6 : 
				result = R[operandOne][0] - operandTwo	+ carry - 1
				print("EXECUTE: SBC ", R[operandOne][0], " and ", operandTwo, sep="")
			elif opcode == 7 : 
				result = operandTwo - R[operandOne][0]	+ carry - 1
				print("EXECUTE: RSC ", R[operandOne][0], " and ", operandTwo, sep="")	
			# elif opcode == 8 : 
			# 	result = operandTwo - R[operandOne][0]	+ carry - 1
			# 	print("EXECUTE: TST ", R[operandOne][0], " and ", operandTwo, sep="")
			# elif opcode == 9 : 
			# 	result = operandTwo - R[operandOne][0]	+ carry - 1
			# 	print("EXECUTE: RSC ", R[operandOne][0], " and ", operandTwo, sep="")
			elif opcode == 10 : 
				print("EXECUTE: CMP ", R[operandOne][0], " and ", operandTwo, sep="")			
				if R[operandOne][0] == operandTwo: 
					Z = 1
				elif R[operandOne][0] < operandTwo :
					N = 1
			elif opcode == 12 : 
				result = R[operandOne][0] | operandTwo
				print("EXECUTE: ORR ", R[operandOne][0], " and ", operandTwo, sep="")	
			elif opcode == 13 : 
				result = operandTwo
				print("EXECUTE: MOV ", operandTwo, " in R", destination, sep="")
			elif opcode == 14 : 
				result = R[operandOne][0] & ~operandTwo
				print("EXECUTE: BIC ", operandTwo, " in R", destination, sep="")	
			elif opcode == 15 : 
				result = ~operandTwo
				print("EXECUTE: MVN ", operandTwo, " in R", destination, sep="")
	elif flag == 1:
		offsetValue = int(operandTwo/4);
		if groupCode == 25:
			result = R[operandOne][offsetValue];
			print("EXECUTE: Put R", operandOne, "'s ", (offsetValue+1), " element in R", destination, sep="");
		elif groupCode == 24:
			result = R[operandOne][offsetValue];
			print("EXECUTE: Put R", operandOne, "'s ", (offsetValue+1), " element in R", destination, sep="");


if __name__ == '__main__':
	file = open("input.mem", "r");
	fetch();
	decode();
	execute();
	print();
	fetch();
	decode();
	execute();
	print();
	fetch();
	decode();
	execute();
	print();
	fetch();
	decode();
	execute();
	print();
	fetch();
	decode();
	execute();
	print();
	file.close();