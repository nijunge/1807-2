import random
pc = random.randint(1,100)
i = 0
for i in range(1,11):
	py = int(input("请输入数字"))
	if py > pc:
		print("猜大了")
	elif py < pc:
		print("猜小了")
	else:
		print("猜对了")
		break
print("一共猜了%d次"%i)
if i<= 5:
	print("你真聪明，这么快就猜出来了")
else:
	print("还需改进方法，争取更快")
