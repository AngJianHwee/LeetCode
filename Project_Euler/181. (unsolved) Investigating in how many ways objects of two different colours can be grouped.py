MAX_LEN = int(1e5)
arr = [-1 for i in range(MAX_LEN)]

arr[0] = 1
arr[1] = 1

def fac(n, arr):
	if arr[n] != -1:
		return arr[n]
	
	else:
		arr[n] = fac(n-1,arr)*n
		return arr[n]

N = 4
total = 0
for i in range(N):
	total += (fac(N,arr)/(fac(N-i,arr)*fac(i,arr)))
print(total)