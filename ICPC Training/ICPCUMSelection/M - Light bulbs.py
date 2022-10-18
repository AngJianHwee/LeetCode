def pprint(*args):
	print("--", end = " ")
	[print(x, end = " ") for x in args]
	print()


for k in range(int(input())):
	[m,n] = [int(x) for x in input().strip().split()]
	x = []
	y = []
	status = [0 for i in range(m)]
	for i in range(n):
		a,b = [int(x) for x in input().strip().split()]
		for q in range(a,b+1):
			status[q] = not status[q]

	print(f"Case #{k+1}: {sum(status)}")




# 2
# 10 2
# 2 6
# 4 8
# 6 3
# 1 1
# 2 3
# 3 4

#####################################################################3
# def pprint(*args):
# 	print("--", end = " ")
# 	[print(x, end = " ") for x in args]
# 	print()


# for k in range(int(input())):
# 	[m,n] = [int(x) for x in input().strip().split()]
# 	x = []
# 	y = []
# 	for i in range(n):
# 		a,b = [int(x) for x in input().strip().split()]
# 		x.append(a)
# 		y.append(b)

# 	# m = 10
# 	# n = 2
# 	# x = [2, 4]
# 	# y = [6, 8]

# 	# pprint("m",m)
# 	# pprint("n",n)
# 	# pprint("x",x)
# 	# pprint("y",y)

# 	s = 0
# 	for i in range(m):
# 		sc = False
# 		for j in range(len(x)):
# 			if x[j] <= i <= y[j]:
# 				sc = not sc
# 		s += int(sc)
# 	print(f"Case #{k+1}: {s}")




# # 2
# # 10 2
# # 2 6
# # 4 8
# # 6 3
# # 1 1
# # 2 3
# # 3 4
