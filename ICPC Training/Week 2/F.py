for _ in range(int(input())):
	N, M = [int(x) for x in input().split()]
	s = input()
	[print(s[i:i+M]) for i in range(len(s)//M)]