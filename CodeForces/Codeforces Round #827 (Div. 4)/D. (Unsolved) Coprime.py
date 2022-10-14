DP_ARR = [[-1 for i in range(j+1)] for j in range(int(1e4))]

def coPrime(a,b,arr):
	b,a = min(a,b), max(a,b)
	if arr[a][b] != -1:
		return arr[a][b]
	else:
		for i in range(2,b):
			if (a % i == 0) and (b%i == 0):
				arr[a][b] = False
				return arr[a][b]
		arr[a][b] = True
		return arr[a][b]



for i in range(int(input())):
	input()
	arr_ori = [int(x) for x in input().strip().split()]
	arr = sorted(list(set(arr_ori)))[::-1]
	done = False
	for i in range(len(arr)):
		if done:break
		for j in range(i+1,len(arr)):
			if done:break
			if coPrime(arr[i],arr[j], DP_ARR):
				print("\t",arr[i],arr[j])
				print("\t",arr_ori.index(arr[i]),arr_ori.index(arr[j]))
				# print("\t",arr_ori[arr[i]],arr_ori[arr[j]])				
				done = True
