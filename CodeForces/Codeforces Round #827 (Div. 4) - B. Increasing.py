for i in range(int(input())):
	input()
	arr = [int(x) for x in input().strip().split()]
	arr = sorted(arr)    
	if len(arr) == len(set(arr)):
		print("YES")
	else:
		print("NO")		
