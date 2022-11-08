import itertools
n = 4
x = [1 for _ in range(2**n)]
arr = [x]
cur = [1 for _ in range(2**n)]
while len(arr) < 2**n:
	for z in set(itertools.permutations(cur,len(cur))):
		status = 1
		for x in arr:
			if (sum([a*b for a,b in zip(z,x)])) != 0:
				status = 0
				break
		if status == 1:
			arr.append(z)
		
		if len(arr) == 2**n:
			break
	cur.pop(0)
	cur.append(-1)
print(arr)






# # # n = int(input())
# # n = 0
# # if n == 0:
# # 	# s = "+"
# # 	s = ""
# if n >= 1:
# 	arr = [[1,1],[1,-1]]
# 	# s = '+*\n'+'*+'
# if n >= 2:
# 	arr = [[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[-1,1,-1,1]]

# # 	s = '++++\n'+'++**\n'+'+*+*\n'+'+**+'
# if n == 3:
# 	arr = [[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[-1,1,-1,1]]

# # 	s = "++++++++\n"+"++++++**\n"+"++**+*+*\n"+"++**+**+\n"+"+*+*++++\n"+"+*+*++**\n"+"+*+*+*+*\n"+"+*+*+**+"
# # print(s)


# n = 2
