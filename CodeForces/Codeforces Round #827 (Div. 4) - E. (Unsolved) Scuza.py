for i in range(int(input())):
	# print("=========================================")
	input()
	arr = [int(x) for x in input().strip().split()]
	arr2 = [int(x) for x in input().strip().split()]
	# print("-----------------------------------------")
	i = 0
	j = 0
	steps = [0 for _ in range(len(arr2))]
	while i != len(arr) and j != len(arr2):
		if arr2[j] >= arr[i]:
			for k in range(j,len(steps)):
				steps[k] += arr[i]
			i += 1
			continue
		else:
			j += 1
	print(" ".join([str(x) for x in steps]))
				



######################################### SAMPLE INPUT ##################################
# 3
# 4 5
# 1 2 1 5
# 1 2 4 9 10
# 2 2
# 1 1
# 0 1
# 3 1
# 1000000000 1000000000 1000000000
# 1000000000
