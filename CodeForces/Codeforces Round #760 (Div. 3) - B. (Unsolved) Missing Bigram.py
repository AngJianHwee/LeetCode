# for i in range(int(input())):
# 	input()
# 	arr = [str(x) for x in input().strip().split()]
# 	done = False
# 	if len(arr) == 1:
# 		print(arr[0][0]+arr[0][::-1])
# 	x = ""
# 	for i in range(len(arr) -1):
# 		done = True
# 		x += arr[i][0]
# 		if arr[i][-1] != arr[i+1][0]:
# 			x += arr[i][1]
# 	x += arr[-1]
# 	if not done:
# 		print("--","Done")
# 		x += arr[-1][-1][::-1]
# 	print("--",x)


# # ######################################### SAMPLE INPUT ##################################



def pprint(*args):
	print("--", end = " ")
	[print(x, end = " ") for x in args]
	print()


for i in range(int(input())):
	input()
	arr = [str(x) for x in input().strip().split()]
	
	x = ""
	if len(arr) == 1:
		print(arr[0]+arr[0][-1])
		continue

	for i in range(len(arr)-1):
		x +=(arr[i])
		if arr[i][-1] == arr[i]:
			x += (arr[i][-1])
			x += (arr[i+1][0])
	x += (arr[-1])
	pprint(x[0] + x[1::2] + x[-1])

######################################### SAMPLE INPUT ##################################