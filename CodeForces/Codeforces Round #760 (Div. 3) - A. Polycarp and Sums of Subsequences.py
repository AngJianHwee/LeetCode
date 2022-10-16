for i in range(int(input())):
	arr = [int(x) for x in input().strip().split()]
	arr = [arr[0], arr[1], arr[-1] - arr[0] - arr[1]]
	arr = sorted(arr)    
	arr = [str(x) for x in arr]
	print(" ".join(arr))
	
######################################### SAMPLE INPUT ##################################