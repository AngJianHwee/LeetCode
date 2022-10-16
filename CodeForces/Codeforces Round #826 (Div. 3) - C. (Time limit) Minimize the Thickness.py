def pprint(*args):
	print("--", end = " ")
	[print(x, end = " ") for x in args]
	print()


for i in range(int(input())):
	input()
	arr = [int(x) for x in input().strip().split()]
	n = len(arr)
	
	i_s = []
	for i in range(1,n):
		if sum(arr)%sum(arr[0:i]) == 0:
			i_s.append(i)
	
	if len(i_s) == 0:
		print(len(arr))
	else:
		min_ls = []
		for i in i_s:
			min_l = 0
			x = sum(arr[0:i])
			j = i
			while j < n:
				k = j+1
				while(sum(arr[j:k])!=x):
					k += 1
				min_l = max(min_l,k-j)
				j = k
			min_ls.append(min_l)
		print(min(min_ls))






######################################### SAMPLE INPUT ##################################

