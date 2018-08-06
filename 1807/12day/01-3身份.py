x = []
for i in range(3):
	d = {}
	name = input("请输入名字")
	age = input("请输入年龄")
	sex = input("请输入性别")
	d["name"] = name
	d["age"] = age
	d["sex"] = sex
	x.append(d)
print(x)
for i in x:
	for j in i:
		print(i[j])

