import os
dir = input("请输入文件夹名字")
files = os.listdir(dir)
os.chdir(dir)
for i in files:
	position = i.rfind(".")
	newname = i[:position]+"-腾讯"+i[position:]
	os.renames(i,newname)
