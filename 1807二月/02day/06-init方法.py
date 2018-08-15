class Dog():
	#作用:初始化属性
	def __init__(self,name,age):
		self,name = name
		self.age = age
	def wark(self):
		print("汪汪叫")
	def eat(self):
		print("吃")
hashiqi = Dog("二哈",10)#创建对象或创建一个实例
hashiqi.wark()
hashiqi.eat()
#hashiqi.age = 10
#hashiqi.name = "哈士奇"
print("hashiqi.age")
print("hsahiqi.name")
