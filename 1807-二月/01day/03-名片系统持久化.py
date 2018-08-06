list = []
f = open("data.data","r") 
content = f.read()
if len(content) != 0:
	list = eval(content)
	for i in list:
		for k,v in i.items():
			print(k,v)
	print(list)
f.close
