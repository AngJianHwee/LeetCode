
while True:
	N, M = [int(x) for x in input().split()]
	g = [[0 for _ in range(N)] for __ in range(M)]
	a,b = [int(x) for x in input().split()]
	if (a,b) == (-1, -1):
		print("end")
	else:
		g[a][b] = 1
		g[b][a] = 1
print(g)