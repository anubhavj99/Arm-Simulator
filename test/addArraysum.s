mov r0, #0
swi 0x6c

mov r3,r0

@Sum variable
mov r1, #0

@Counter
mov r2, #0

@loop to find the sum
loop:
cmp r2,r3
bge loop_exit
mov r0, #0
swi 0x6c
add r1,r1,r0
add r2,r2,#1
b loop
loop_exit:

@Printing on stdout
mov r0,#1
swi 0x6b
str r1, [r5, #12]
ldr r1, [r5, #12]
swi 0x11