for _ in range(int(input())):
	n = int(input().strip())
	arr = []
	for j in range(n):
		arr.append([int(x) for x in input().strip().split()])
	print(arr)
	def move(cur,visited, cup,cdown):
		if cup >= cdown:
			return 0
		if cur[0] == 0:
			return max()