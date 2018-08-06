students = []
def showError(msg):
	print("输入有误，请重新输入"+msg)
def isNum(num):
	if num.isdigit():
		return True
	else:
		return False
def add():
	stu = {}
	while True:
		name = input("请输入学生姓名")
		if len(name) >= 2 and len(name) <= 4:
			stu["name"] = name
			break
		else:
			showError("姓名必须大于2小于4")
	while True:
		age = input("请输入年龄")
		if isNum(age):
			age = int(age)
		else:
			print("输入有误")
			continue
		if age > 1 and age < 150:
			stu["age"] = age
			break
		else:
			showError("年龄必须大于1小于150")
	while True:
		sex = input("请输入性别")
		if sex == "男" or sex == "女":
			stu["sex"] = sex
			break
	while True:
		phone = int(input("请输入电话"))
		if len(phone) = 11 and phone.startswith(1):
			stu["phone"] = phone
			break
		else:
			showError("手机号码必须是1开头并且11位数字")
		students.append(stu)
		print(students)
		print("添加成功")
def find():
	name = input("请输入学生姓名")
	for stu in students:
		if stu["name"] == name:
			print("学生名字是:%s\n学生年龄是:%d\n学生性别是:%s\n学生电话是:%d"%(stu["name"],stu["age"],stu["sex"],stu["phone"]))
			break
def change():
	name = input("请输入学生姓名")
	flag = False
	for stu in students:
		if stu["name"] == name:
			flag = True
			while True:
				print("1:修改名字")
				print("2:修改年龄")
				print("3:修改性别")
				print("4:修改电话")
				number = input("请选择修改序号")
				if isNum(num):
					num = int(num)
				else:
					print("输入有误")
					continue
				if number == 1:
					stu["name"] =input("请输入新的名字")
				elif number == 2:
					stu["age"] = int(input("请输入新的年龄"))
				elif number == 3:
					stu["sex"] = input("请输入新的性别")
				elif number == 4:
					stu["phone"] = int(input("请输入新的电话"))
					print("修改成功")	
				break
			break
	if not flag:
		print("查无此人")
def delete(): 
	name = input("请输入学生姓名")
	for stu in students:
		if stu["name"] == name:
			students.remove(stu)
			print("删除成功")
			break
def print_students():
	print("姓名        年龄        性别        手机号")
	for stu in students:
		print("%s        %d        %s        %d"%(stu["name"],stu["age"],stu["sex"],stu["phone"]))
def show_exit():
	print("谢谢使用")
	break
def print_menu():
	print("欢迎使用学生管理系统".center(30," "))
	while True:
		print("1、添加学生信息")
		print("2、查看学生信息")
		print("3、修改学生信息")
		print("4、删除学生信息")
		print("5、显示全部信息")
		print("6、退出管理系统")
		input_info()
def input_info():
	num = input("请选择功能")
	if isNum(num):
		num = int(num)
	else:
		print("输入有误")
	if num.isdigit():
		num = int(num)
	else:
		print("输入有误")
	if num == 1:
		add()
	elif num == 2:
		find()
	elif num == 3:
		change()
	elif num == 4:
		delete()
	elif num == 5:
		print_students()
	elif num == 6:
		exit()
print_menu()
