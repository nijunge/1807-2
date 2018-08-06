a = 1000
def test():
	global a 
	a = 100
	print(a)
test()
print(a)

name = "老王1"
def test1():
	global name
	name = "老王2"
	print(name)
test1()
print(name)
