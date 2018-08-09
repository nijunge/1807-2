class Person:
	def eat(self):
		print("吃")
	def play(self):
		print("玩")
	def sleep(self):
		print("睡觉")
	def introduce(self):
		print("我的名字是%s,我的年龄是%d,我的身高是%d"%(self.name,self.age,self.height))
wzz = Person()
wzz.eat()
wzz.play()
wzz.sleep()
wzz.name = "王志洲"
wzz.age = 17
wzz.height = 170
wzz.introduce()
print(wzz.name)
print(wzz.age)
print(wzz.height)

wz = Person()
wz.eat()
wz.play()
wz.sleep()
wz.name = "王哲"
wz.age = 19
wz.height = 170
wz.introduce()

yc = Person()
yc.eat()
yc.play()
yc.sleep()
yc.name ="袁充"
yc.age = 22
yc.height = 175
yc.introduce()

