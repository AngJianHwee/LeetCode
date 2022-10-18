while True:
	try:
		arr = [int(x) for x in input().strip().split()]
		arr = sorted(arr)
		print(arr[1]-arr[0])
	except :
		break