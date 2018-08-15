import random
class DiGua():
	def __init__(self):
		self.status = "生的"
		self.times = 0
		self.z1 = []
	def __str__(self):
		msg = "我烤的程度是%s"%self.status
		return msg+str(self.z1)
	def cook(self,time):
		self.times+=time
		if self.times >= 1 and self.times <= 2:
			self.status = "生的"
		elif self.times >= 3 and self.times <= 5:
			self.status = "半生不熟"
		elif self.times >= 6 and self.times <= 8:
			self.status = "8分熟"
		elif self.times >= 9 and self.times <= 12:
			self.status = "正好"
		elif self.times > 12:
			self.status = "烤焦了"
	def addz1(self,name):
		self.z1.append(name)
list = ["盐","糖","番茄酱","黑胡椒","辣椒","孜然"]
digua = DiGua()
for i in range(1,5):
	digua.cook(random.randint(1,4))
	z1 = random.choice(list)
	list.remove(z1)
	digua.addz1(z1)
	print(digua)

