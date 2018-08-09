class Car():
	def __init__(self,color,type):
		self.color = color
		self.type = type 
	def __str__(self):
		msg = "我的颜色是:%s,我的型号是:%s"%(self.color,self.type)
		return msg
	def move(self):
		print("车在跑")
	def music(self):
		print("在车里听音乐")
#	def introduce(self):
#		print("我的颜色是%s,我的型号是%s"%(self.color,self.type))
lbjn = Car("orange","兰博基尼蝙蝠")
#lbjn.move()
#lbjn.music()
#lbjn.introduce()
print(lbjn)
