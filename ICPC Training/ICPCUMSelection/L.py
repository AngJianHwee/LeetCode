_,m = [int(x) for x in input().strip().split()]
arr = [int(x) for x in input().strip().split() if x != ""]
z = min(arr)

for i in range(m):
	x = int(input().strip())
	if x < z:
		# print("--",-1)
		print(-1)
		continue
	else:
		y = z
		for j in arr:
			if j <= x:
				y = max(j,y)
			if y == x:
				break
			# elif arr[j] == x:
				# print("--",x)
				# break
		# print("--",y)
		print(y)
