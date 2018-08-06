list = [1,3,4,7,10,45,60,80,100]
min = 0
max = len(list)-1
count = 80
while True:
	center = int((min+max)/2)
	if list[center] > count:
		max = center - 1
	elif list[center] < count:
		min = center +1
	elif list[center] == count:
		print("索引是%d"%center)
		break
                          
