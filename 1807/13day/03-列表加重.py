list =[1,2,3,4,5,6,2,5,7,6,3,7,5,4]
list1 =[]
for i in list:
	if i not in list1:
		list1.append(i)
		print(list1)
