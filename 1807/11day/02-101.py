i = 0
j = []
while i < 101:
	if i%2 == 0:
		j.append(i)
	i+=1
	print(j)
j.pop(0)
j.remove(20)
print(j)
