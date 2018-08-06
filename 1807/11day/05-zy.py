names = ["老王","老宋"]
print(names)

for i in names:
	print("%s你好"%i)

car = ["骑摩托","开汽车","骑电车"]
for a in car:
	print("我喜欢%s"%a)

name = ["老王","老宋","老赵"]
for b in name:
	print("%s我想邀你共进晚餐"%b)

name.pop(0)
name.insert(0,"老张")
print("老王无法赴约")
for b in name:
	print("%s我想邀你共进晚餐"%b)

name.insert(0,"老刘")
name.insert(2,"老马")
name.append("老袁")
print("我找到了一个更大的餐桌")
for b in name:
	print("%s我想邀你共进晚餐"%b)

c = ["老刘","老张","老马","老宋"]
for b in c:
	print("%s新购买的餐桌无法及时送达,我很抱歉，无法邀请你来共进晚餐"%b)
name.pop(0)
name.pop(0)
name.pop(0)
name.pop(0)
for b in name:
	print("%s我想邀你共进晚餐"%b)
print(len(name))
del name[0]
del name[0]
print(name)

tra = ["洛杉矶","迈阿密","巴黎","东京","土耳其"]
print(tra)

tra.reverse()
print(tra)
tra.reverse()
print(tra)
tra.sort()
print(tra)
tra.sort(reverse=True)
print(tra)

l = ["汉语","英语","法语","韩语"]
print(l)
l.pop(3)
print(l)
l.insert(0,"俄语")
print(l)
