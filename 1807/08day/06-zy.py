'''
import random
i = 0
num = random.randint(1,100)
while i < 9:
	u_num = int(input("请输入猜的数字"))
	if u_num > num:
		print("猜大了兄弟")
	elif u_num < num:
		print("猜小了兄弟")
	else:
		print("你真叼，兄弟")
		break
	i+=1
'''		


import random 
num = random.randint(1,100)
for i in range(1,10):
	u_num = int(input("请输入猜的数字"))
	if u_num > num:
		print("猜大了兄弟")
	elif u_num < num:
		print("猜小了兄弟")	
	else:
		print("你真叼，兄弟")
		break
