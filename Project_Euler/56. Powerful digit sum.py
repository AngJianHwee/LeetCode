N = 100
x = []
for i in range(N):
	for j in range(N):
		x.append(sum([int(x) for x in str(i**j)]))
print(max(x))