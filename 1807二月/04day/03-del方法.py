class Dog():
	def __init__(self):
		self.name = "二哈"
		print("init")
	def __str__(self):
		return "我是str"
	def __del__(self):
		print("我是del")
hsq = Dog()
print(hsq)
xtq = hsq
del hsq
del xtq
print("啦啦啦")

