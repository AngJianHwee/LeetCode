x,y = [int(x) for x in input().strip().split()]
arr = [int(x) for x in input().strip().split()]
num = 0
if len(arr) == 1:
	print(1)
else:
	for i in range(len(arr)-1):
		if arr[i+1] - arr[i] > y:
			num = 0
		else:
			num += 1
	print(num+1)
######################################### SAMPLE INPUT ##################################