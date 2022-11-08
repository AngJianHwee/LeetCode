while True:
	N, M = [int(x) for x in input().split()]
	if (N,M) == (0,0):
		break

	a = []
	for _ in range(N):
		a.append(input())
	input()
	
	print(a)
	
