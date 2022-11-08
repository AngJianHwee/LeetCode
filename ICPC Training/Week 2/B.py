L, T, O = [int(x) for x in input().split()]

b = [0 for _ in range(L)]

for _ in range(O):
	a = [x for x in input().split()]
	if a[0] == 'C':
		a = [int(x) for x in a[1:]]
		a[0] -= 1
		a[1] -= 1
		for j in range(a[0], a[1]+1):
			try:
				b[j] = a[-1]
			except:
				pass
	else:
		None
		print(len(set(b[int(a[1])-1:int(a[2])])))

