input()
arr = [int(x) for x in input().strip().split()]
x = arr[0]
s = 0
for i in range(1,len(arr)):
	if arr[i] < x:
		# print(x, arr[i], abs(x - arr[i]))
		s += abs(x - arr[i])
	x = max(x, arr[i])
print(s)
