i = 0
while i < 10:
	j = 1
	while j < i+1:
		print("%d*%d=%d"%(j,i,i*j),end ="\t")
		j+=1
	print("")
	i+=1
