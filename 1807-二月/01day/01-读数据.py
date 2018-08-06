name = input("请输入备份文件名字(要有后缀名)")
f = open(name,"r")
content = f.read()

fl = open("备份.txt","w")
fl.write(content)

f.close()
fl.close()
