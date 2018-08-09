class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None#刚初始化人对象没有枪
		self.hp = 100
	def zhuangzidan(self,dj,zd):#装子弹
		dj.addzidan(zd)#弹夹装子弹

	def zhuangdanjia(self,dj,gun):#装弹夹
		gun.addDanJia(dj)#枪自己装弹夹

	def naqiang(self,gun):#拿枪
		self.gun = gun

	def kaiqiang(self,diren):#老王开枪
		self.gun.kaihuo(diren)

	def diaoxue(self,count):#count是子弹伤害量
		self.hp -= count
		if self.hp <= 0:
			print("挂了")
		else:
			print("还剩%d"%self.hp)
class Gun():
	def __init__(self,name):
		self.name = name
		self.dj = None

	def addDanJia(self,dj):
		self.dj = dj

	def kaihuo(self,diren):#枪开火
		zidan = self.dj.tanzidan()#弹出一个子弹
		zidan.sharen(diren)#子弹杀人

class DanJia():
	def __init__(self,count):
		self.count = count
		self.zds = []#子弹列表

	def addzidan(self,zd):
		self.zds.append(zd)

	def tanzidan(self):
		return self.zds.pop(0)
class ZiDan():
	def __init__(self,name,sh):
		self.name = name	
		self.sh = sh 

	def sharen(self,diren):
		diren.diaoxue(self.sh)#掉血
laowang = Person("老王")#创建一个老王对象
ak47 = Gun("ak47")#创建枪对象
dj = DanJia(30)#创建一个弹夹
for i in range(30):#创建一些子弹
	zd = ZiDan("7.62",10)
	laowang.zhuangzidan(dj,zd)#老王装子弹
laowang.zhuangdanjia(dj,ak47)#老王装弹夹
laowang.naqiang(ak47)#老王开枪
laosong = Person("老宋")#创建一个敌人
laowang.kaiqiang(laosong)#老王开枪
laowang.kaiqiang(laosong)#老王开枪
laowang.kaiqiang(laosong)#老王开枪
laowang.kaiqiang(laosong)#老王开枪
laowang.kaiqiang(laosong)#老王开枪
laowang.kaiqiang(laosong)#老王开枪
laowang.kaiqiang(laosong)#老王开枪
laowang.kaiqiang(laosong)#老王开枪
laowang.kaiqiang(laosong)#老王开枪
laowang.kaiqiang(laosong)#老王开枪
