#coding=utf-8
try:
	open("1.txt","r")
	#print("laowang")
	print(1+1)
except(FileNotFoundError,NameError):
	print("报错了")
except Exception as ret:
	print("报错了",ret)
else:
	print("没有错误的执行")
finally:
	print("不管对错都执行")
