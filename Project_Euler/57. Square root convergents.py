N = 1000


def simplified(n,arr):
	if arr[n]!=-1:
		return arr[n]
	if n == 1:
		return [1,2]
	else:
		x = simplified(n-1, arr)
		x[0] += 2*x[1]
		x = x[::-1]
		arr[n] = x
		return x

arr = [-1 for i in range(int(N)+1)]

count = 0
for i in range(1, int(N)+1):
	x = simplified(i,arr)
	x = [sum(x),x[1]]
	if len(str(x[0]))> len(str(x[1])):
		count += 1
print(count)