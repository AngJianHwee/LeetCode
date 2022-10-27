arr = list(map(float, input().split()))[1:]
arr2 = list(map(float, input().split()))[1:]

while len(arr) < max(len(arr), len(arr2)):
	arr.append(0)

while len(arr2) < max(len(arr), len(arr2)):
	arr2.append(0)

x = [0 for i in range(int(max(arr[::2]+arr2[::2]))+1)]

for i in range(0,len(arr),2):
	x[int(arr[i])] += arr[i+1]
	x[int(arr2[i])] += arr2[i+1]

print(len([x_ for x_ in x if abs(x_-0)>1e-2]), " ".join([" ".join([str(i),str(x[i])]) for i in range(len(x))][::-1]))
