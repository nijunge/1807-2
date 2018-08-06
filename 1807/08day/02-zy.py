i = 0
a = 0
b = 0
while i<100:
	i+=1
	if i %2 == 0:
		print(i)
		a += i
	else:
		b += i
c = b-a
print(c)
