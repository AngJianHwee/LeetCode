def dp(a1,a2,p1,p2):
	if dp_arr[p1][p2] != -1:
		return dp_arr[p1][p2]
	if p1 == len(a1) or p2 == len(a2):
		dp_arr[p1][p2] = 0
		return 0
	if a1[p1] == a2[p2]:
		dp_arr[p1][p2] = 1 + dp(a1,a2,p1+1,p2+1)
		return dp_arr[p1][p2]
		return 1 + dp(a1,a2,p1+1,p2+1)
	else:
		dp_arr[p1][p2] = max(dp(a1,a2,p1+1,p2),dp(a1,a2,p1,p2+1))
		return dp_arr[p1][p2]
		# return max(dp(a1,a2,p1+1,p2),dp(a1,a2,p1,p2+1))

for i in range(int(input())):
	input()
	arr1 = [int(x) for x in input().split()]
	arr2 = [int(x) for x in input().split()]
	
	dp_arr = [[-1 for i in range(max(len(arr1), len(arr2))+1)] for j in range(max(len(arr1), len(arr2))+1)]

	print(f"Case {i+1}: {dp(arr1,arr2,0,0)}")


# from random import randint as ri
# a1 = list(set([ri(100, 250) for i in range(250)]))
# a2 = list(set([ri(100, 250) for i in range(250)]))
# print(a1)
# print(a2)
# print(dp(a1,a2,0,0))