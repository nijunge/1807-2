def calNum(num):
	if num == 1:
		return 1
	else:
		return num*calNum(num-1)
result = calNum(5)
print(result)
