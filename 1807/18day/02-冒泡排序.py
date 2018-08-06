list = [10,6,20,40,80,34,3,25]
for i in range(0,len(list)-1):
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
			list[i],list[j] = list[j],list[i]
	print(list)

