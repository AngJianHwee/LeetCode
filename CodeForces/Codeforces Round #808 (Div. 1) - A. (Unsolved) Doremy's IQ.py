def test(q,arr,i,back):
	# print("--",q,i)
	if i == (len(arr)- 1):
		if q>0:
			back[i] = 1
			return 1
		else:
			back[i] = 0
			return 0
	else:
		if arr[i] > q:
			a,b = (test(q,arr,i+1, back), 1 + test(q-1, arr, i+1,back))
			
			if b > a:
				back[i] = 1
			else:
				back[i] = 0
			
			return max(a,b)

		else:
			back[i] = 1
			return 1+test(q,arr,i+1, back)

for i in range(int(input())):
	n, q = [int(x) for x in input().strip().split()]
	arr = [int(x) for x in input().strip().split() if x != ""]
	back = [-1 for x in arr]
	
	test(q,arr,0,back)
	print("".join([str(x) for x in back]))

######################################### SAMPLE INPUT ##################################