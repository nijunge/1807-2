acc = "123456"
pwd = "123456"
i = 0
while True:

	a = int(input("请输入账号"))
	b = int(input("请输入密码"))

	if a == acc and b == pwd:
		print("登陆成功")
		print("请选择英雄\n0:ADC\n1:肉盾:\n3:法师")
		c = int(input("请选择你的英雄范围"))
		if c == 0:
			print("鲁班七号")
		elif c == 1:
			print("程咬金")
		else:
			print("王昭君")
	else:
		i+=1
		print("登录失败%d次"%i)
		if i == 3:
			break

