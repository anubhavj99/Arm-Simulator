mov R5, #10
mov R4, #2
mov R6, #0 @t
mov R7, #1 @s
mov R8, #0 @ans
loop:CMP R4, R5
	BGT zerocon	
	add R6, R7, R8
	mov R8, R7
	mov R7, R6
	add R4, R4, #1
	BLT loop
zerocon: 
swi 0x11