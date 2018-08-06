students = []
while True:
	print("欢迎来到学生管理系统")
	print("1:添加学生信息")
	print("2:修改学生信息")
	print("3:查找学生信息")
	print("4:删除学生信息")
	print("5:查看全部信息")
	print("6:退出学生管理系统")
	number = int(input("请选择功能"))
	if number == 1:
		stu = {}
		stu["name"] = input("请输入名字")
		stu["age"] = int(input("请输入年龄"))
		stu["sex"] = input("请输入性别")
		stu["phone"] = int(input("请输入电话"))
		students.append(stu)
		print(students)		
	elif number == 2:
		name = input("请输入学生姓名")
		for stu in students:
			if stu["name"] == name:
				print("学生名字:%s\n学生年龄:%d\n学生性别:%s\n学生电话:%d"%(stu["name"],stu["age"],stu["sex"],stu["phone"]))
				print("1:修改名字")
				print("2:修改年龄")
				print("3:修改性别")
				print("4:修改电话")
				number == int(input("请选择修改序号"))
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
	elif number == 3:
		name = input("请输入学生姓名")
		for stu in students:
			if stu["name"] == name:
				print("学生名字是:%s\n学生年龄是:%d\n学生性别是:%s\n学生电话是:%d"%(stu["name"],stu["age"],stu["sex"],stu["phone"]))
				break	
	elif number == 4:
		name = input("请输入学生姓名")
		for stu in students:
			if stu["name"] == name:
				students.remove(stu)
				print("删除成功")
				break
	elif number == 5:
		print("打印全部信息")
        print("姓名        年龄        手机号")
        for stu in students:
            print(stu["name"],end="        ")            
            print(stu["age"],end="        ")            
            print(stu["phone"],end="        ")            
            print("")
	elif number == 6:
		print("谢谢使用")
		break
