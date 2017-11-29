a  = bin(16777208)
a = str(a)
a = a[2:];
print(a)
negative = False;
if a[0] == "1":
	negative = True;
for i in range(len(a)):
	if a[i] == "1":
		a = a[:i] + "0" + a[i+1:]
	elif a[i] == "0":
		a = a[:i] + "1" + a[i+1:]
a = int(a,2)+1;
if negative:
	a = a * -1;
print(bin(a))
print(a)
