m, n = [int(x) for x in input().strip().split()]
arr = [[0 for j in range(m+1)] for i in range(m+1)]
pop = []
for i in range(n):
    x,y = [int(x) for x in input().strip().split() if x != ""]
    arr[x][y] = 1
    arr[y][x] = 1

num = 0
print(arr)
for i in range(1,m+1):
	if i in pop:
		continue
	if sum(arr[i]) == 2:
		print(arr[i])
		j = arr[i].index(1)
		if sum(arr[j]) == 2:
			pop.append(j)
			num += 1
		arr[j][i] = 0
		arr[i][j] = 0
		num += 1
		pop.append(i)
print(arr)
print(num)

######################################### SAMPLE INPUT ##################################
# 3 3
# 1 2
# 2 3
# 3 1
# #############
# 6 5
# 1 4
# 2 4
# 3 4
# 5 4
# 6 4
