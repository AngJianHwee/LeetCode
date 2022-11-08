for _ in range(int(input())):
	n = int(input().strip())
	arr = []
	inv = False
	for j in range(n):
		if inv:
			arr.extend([int(x) for x in input().strip().split()][::-1])
		else:
			arr.extend([int(x) for x in input().strip().split()])
		inv = not inv	
	
	h = 0
	for i in range(len(arr)-1):
		if arr[i] < arr[i+1]:
			h += 1
		else:
			h -= 1
	arr = list(map(str,arr))
	if h < 0:
		print(" ".join(arr))
	else:
		print(" ".join(arr[::-1]))