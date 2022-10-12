# arr = [-1 for i in range(int(1e6)+1)]
# arr[0] = 1
# arr[1] = 1

# def chain(n, arr):
# 	# print("Called", n)
# 	if arr[n] != -1:
# 		return arr[n]
# 	else:
# 		if n%2 == 1:
# 			arr[n] = 1+ chain(int(3*n+1), arr)
# 		else:
# 			arr[n] = 1+ chain(int(n/2), arr)
# 		return arr[n]

# for i in range(int(10000)):
# 	# if arr[int(1e5)] != -1:
# 		# break
# 	chain(i,arr)
# print(arr[:10000])