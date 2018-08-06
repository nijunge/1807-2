def clum(x,y,z):
	ret = z(x,y)
	return ret
ret = clum(1,2,lambda x,y:x+y)
print(ret)


fun = lambda x,y:x+y
print(fun(1,2))
