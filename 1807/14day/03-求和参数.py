def showSum(start,end):
	sum = 0
	for i in range(start,end+1):
		sum+=i
	print(sum)

start = int(input("请输入起始值"))
end = int(input("请输入终止值"))
showSum(start,end)
