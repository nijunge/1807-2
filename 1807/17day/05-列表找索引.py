
list = [1,2,3,4,56,7,8,65,4,6,9,26]
'''
num = int(input("请输入一个数字"))

if num in list:
	position = list.index(num)
	print("索引是%d"position)
	print(list)
else:
	print("不在列表中")
'''


if num in list:
	for p,i in enumerate(list):
		if i == num :
		print("索引是%d"%p)
		print(list)
		break
else:
	print("不在列表中")



