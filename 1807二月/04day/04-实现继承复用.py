class Phone():

	def __init__(self,name,color="金色"):
		self.name = name
		self.color = color
	def Music(self):
		print("%s的%s在放音乐"%(self.color,self.name))

class OPPO(Phone):
	pass

class Vivo(Phone):
	pass

r9s = OPPO("r9s")
print(r9s.name)
print(r9s.color)

x7 = Vivo("x7")
print(x7.name)
print(x7.color)
