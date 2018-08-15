class Manger():
	def __init__(self):
		self.name = "学生管理大师v1.0"
		self.list = []
	def add(self,stu):
		
		self.list.append(stu)
	def find(self):
		self.name = input("请输入要查找的名字")
		for stu in self.list:
			if stu[self.name] = self.name
				print("姓名是:%s\n年龄是%d\n性别是\n"%(self.name,self.age,self.sex))
				break
	def change(self):
		self.name = input("请输入要查找的名字")
		for stu in self.list:
			if stu[self.name] = self.name
				print("姓名是:%s\n年龄是%d\n性别是\n"%(self.name,self.age,self.sex))
				print("1:修改名字")
				print("2:修改年龄")
				print("3:修改性别")
				self.number = input("请选择序号")
				if self.number == 1:
					stu[self.name] = input("请输入新的名字")	
				elif self.number == 2:
					stu[self.age] = input("请输入新的年龄")	
				elif self.num ==3:
					stu[self.sex] = input("请输入新的性别")
				print("修改成功")
				break
	def delete(self):
		self.name = input("请输入要删除的名字")
		for stu in self.list:
			if stu[self.name] = name:
				self.list.remove(stu)
				print("删除成功")
				break
class Student():
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex
m = Manger()	
while True:
	name = input("请输入学生姓名")
	age = input("请输入学生年龄")
	sex = input("请输入学生性别")
	stu = Student(name,age,sex)
	m.add(stu)
