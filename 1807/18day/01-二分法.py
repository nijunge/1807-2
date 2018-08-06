list = [1,3,4,6,8,9,10,14]
min = 0
max = len(list)-1
count = 9
while True:
	center = int((min+max)/2)
	if list[center] > count:
		max = center - 1
	elif list[center] < count:
		min = center +1
	elif list[center] == count:
		print("索引是%d"%center)
		break
