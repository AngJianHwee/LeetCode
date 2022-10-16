
def startWith(arr, sign):
	count = 0
	i = 0
	while i < len(arr):
		if arr[i]*sign > 0:
			count += 1
			sign = -1*sign
		i += 1
	return count


def calc(arr, sign):
	total = 0
	i = 0
	while i < len(arr):
		x = None
		while (i < len(arr)) and (arr[i] * sign > 0):
			if x is not None:
				x = max(x, arr[i])
			else:
				x = arr[i]
			i += 1
		sign = -1*sign
		total += x
	return(total)



for i in range(int(input())):
	input()
	arr = [int(x) for x in input().strip().split()]
	if startWith(arr, 1) > startWith(arr, -1):
		sign = 1
		print(calc(arr,sign))
	elif startWith(arr, 1) < startWith(arr, -1):
		sign = -1
		print(calc(arr,sign))
	else:
		print(max(calc(arr, 1), calc(arr, -1)))


######################################### SAMPLE INPUT ##################################
# arr = [1, 2, 3, -1, -2]
# arr = [-1,-2,-1,-3]
# arr = [-2,8,3,8,-4,-15,5,-2,-3,1]
# arr = [1,-1000000000,1,-1000000000,1,-1000000000]

