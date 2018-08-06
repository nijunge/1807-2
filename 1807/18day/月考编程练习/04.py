import random
pc = random.randint(1,3)
i = 0
for i in range(1,4):
	py = int(input("请输入1:石头 2:剪刀 3:布"))
	if py > 0 and py < 4:
		if (py == 1 and pc == 2) or (py == 2 and pc == 3) or (py == 3 and pc == 1):
			print("玩家赢")
		elif py == pc:
			print("平局")
		else:
			print("电脑赢")
	else:
		print("输入不合法")
