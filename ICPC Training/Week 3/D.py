# import queue
# q = queue.Queue()
# print(q)
# q.put([0,0])
# print(q.get())




n, p, t = [float(x) for x in input().strip().split()]

n = int(n)
t = int(t)
arr = [(n,1)]
arr_next = []

for i in range(t):
	for a,b in arr:
		if a == 0:
			arr_next.append((a,b))
		else:
			arr_next.append((a,b*(1-p)))
		if a != 0:
			arr_next.append((a-1,b*p))
	del(arr)
	dic = {}
	for a,b in arr_next:
		try:
			dic[a] += b
		except:
			dic[a] = b
	arr_next = list(dic.items())
	del(dic)
	arr = arr_next.copy()
	arr_next = []

# print(arr)
print(n - sum([a*b for a,b in arr]))