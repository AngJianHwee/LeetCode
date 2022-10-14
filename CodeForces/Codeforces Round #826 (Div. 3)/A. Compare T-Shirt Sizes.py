for i in range(int(input())):
	arr = [x for x in input().strip().split()]
	if arr[0] == arr[1]:
		print("=")
	else:
		size = ['S','M','L']
		a,b = size.index(arr[0][-1])-1, size.index(arr[1][-1])-1
		for x in arr[0][:-1]:
			if x == "X":
				a *= 2
		for x in arr[1][:-1]:
			if x == "X":
				b *= 2
		if a == b:
			print("=")
		elif a > b:
			print(">")
		else:
			print("<")
######################################### SAMPLE INPUT ##################################
# 6
# XXXS XS
# XXXL XL
# XL M
# XXL XXL
# XXXXXS M
# L M
