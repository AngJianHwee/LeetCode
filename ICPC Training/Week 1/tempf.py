def fac(n, arr):
	if arr[n] != -1:
		return arr[n]
	elif n == 1:
		arr[n] = 1
	else:
		arr[n] = (n)*fac(n-1, arr)
	return arr[n]



x = int(input().strip())
DP = [-1 for i in range(int(x)+1)]
print((fac(x, DP)*fac(x, DP))/(x**x))
