class Manger():
	def __init__(self):
		self.name = "学生管理大师v1.0"
		self.list = []
	def add(self,stu):
		self.list.append(stu)
	def find(self):
		pass
	def change(self):
		pass
	def delete(self):
		pass
class Student():
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex
while True:
	name = input("请输入学生姓名")
	age = input("请输入学生年龄")
	sex = input("请输入学生性别")
	stu = Student()
