"""

1----石头
2----剪刀
3----步

玩家: 1----2 2----3 3----1

电脑: 1
"""
'''
import random
while True:
	pc = random.randint(1,3)
	player = int(input("请输入1:石头 2:剪刀 3:布"))
	if (player < 4 and player > 0):
		if (player == 1 and pc ==2) or (player == 2 and pc ==3) or (player == 3 and pc ==1):
			print("玩家赢")
		elif player == pc:
			print("平局")
		else:
			print("电脑赢")
	else:
		print("输入不合法")
'''
import random
for pc in range(1,4):
	pc = random.randint(1,4)
	py = int(input("请输入1:石头 2:剪刀 3:布"))
	if py < 4 and py > 0:
			if (py == 1 and pc == 2) or (py == 2 and pc ==3) or (py == 3 and pc == 1):
				print("玩家赢")
			elif py == pc:
				print("平局")
			else:
				print("电脑赢")
	else:
		print("输入不合法")
