N = 1e5
def fac(n,arr):
	if n < 0:
		return 1

	if arr[n] != -1:
		return arr[n]

	if n == 0:
		ans = 1
	elif n == 1:
		ans = 1
	else:
		ans = n* fac(n-1,arr)
	arr[n] = ans
	return ans

arr = [-1 for i in range(int(N+1))]

def nCr(n,r):
	return fac(n,arr) / (fac(r,arr) * fac(n-r,arr))

count = 0
for i in range(10,100+1):
	for r in range(i+1):
		if (nCr(i,r)) > 1000000:
			count += 1	

print(count)