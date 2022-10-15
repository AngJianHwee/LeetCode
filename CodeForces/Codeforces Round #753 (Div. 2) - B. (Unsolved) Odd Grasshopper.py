for i in range(1):
# for i in range(int(input())):
	# x,y = [int(x) for x in input().strip().split()]
	x,y = 0,1
	if y < 100:
		for i in range(1,y+1):
			if x%2 == 0:
				x -= i
			else:
				x += i
		print(x)
######################################### SAMPLE INPUT ##################################