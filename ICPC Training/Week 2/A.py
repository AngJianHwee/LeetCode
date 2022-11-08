arr = ["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
for _ in range(int(input())):
	x,y = input().split()
	x = arr.index(x)
	y = arr.index(y)
	if x < y:
		print(y-x)
	elif y < x:
		print(12 + y-x)
	else:
		print(12)



