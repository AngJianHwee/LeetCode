DP_ARR = [[-1 for i in range(1e5)] for j in range(int(1e5))]
DP_ARR = [[-1 for i in range(j+1)] for j in range(int(1e5))]

for i in range(int(input())):
	input()
    x = int(input().strip())
    x = float(input().strip())
    arr = [int(x) for x in input().strip().split()]
    arr = [int(x) for x in input().strip().split() if x != ""]
	arr = sorted(arr)    

	print("YES")
	print("NO")

	print("True")
	print("False")

	for i in range(len(arr)):
	for i in range(len(arr)-1):

######################################### SAMPLE INPUT ##################################
# 5
# 4
# 3
# 7
# 5
# 2
