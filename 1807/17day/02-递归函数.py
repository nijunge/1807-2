def test1(d):
	d*1
def test2(c):
	c*test(c-1)
def test1(b):
	b*test(b-1)
def test(a):
	if a == 1:
		return a
	else:
		a*test(a-1)
ret = test(5)
test(ret)
