list = []
list1 = [20,52,94,82,73,69]
list.extend(list1)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
for i in list:
	print(i)
print(len(list))
print(list.count(20))
print(max(list))
print(min(list))
