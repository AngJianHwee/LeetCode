# import queue
# q = queue.Queue()
# print(q)
# q.put([0,0])
# print(q.get())

# n, p, t = [float(x) for x in input().strip().split()]
n,p,t = 4, 0.20, 1
n,p,t = 1, 0.5, 4

n = int(n)
t = int(t)
arr = [(n,1)]
arr_next = []

for i in range(t):
	for a,b in arr:
		arr_next.append((a,b*(1-p)))
		if a != 0:
			arr_next.append((a-1,b*p))
	arr = arr_next.copy()
	arr_next = []
print(arr)
print(sum([a*b for a,b in arr]))