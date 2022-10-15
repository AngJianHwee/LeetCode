# ###################################### DP Sol with cutting edge, not working ######################################
# DP_ARR = [None for i in range(int(1e5))]
# DP_ARR[1] = 0



# def count(n,arr):
# 	if arr[n] is not None:
# 		return arr[n]
# 	for i in (2,3,5):
# 		if n%i == 0:
# 			if count((i-1)*n//i, arr) == -1:
# 				arr[n] = -1
# 				return arr[n]
# 			else:
# 				arr[n] = count((i-1)*n//i, arr) + 1
# 				return arr[n]
# 	arr[n] = -1
# 	return arr[n]




# print(count(1,DP_ARR))
# print(count(10,DP_ARR))
# print(count(25,DP_ARR))
# print(count(30,DP_ARR))
# print(count(14,DP_ARR))
# print(count(27,DP_ARR))
# print(count(1000000000000000000,DP_ARR))


###################################### DP Sol without cutting edge ######################################
def count(n):
	if n == 1:
		return 0
	for i in (2,3,5):
		if n%i == 0:
			x = count((i-1)*n//i)
			if x == -1:
				return -1
			else:
				return x + 1
	return -1


for i in range(int(input())):
	x = int(input().strip())
	print(count(x))

######################################### SAMPLE INPUT ##################################
# 7
# 1
# 10
# 25
# 30
# 14
# 27
# 1000000000000000000