for i in range(int(input())):
	x = int(input().strip())
	y = int(input().strip())
	if x%2 == 0:
		print(f"Case {i+1}: {sum(list(range(x+1,y+1,2)))}")
	else:
		print(f"Case {i+1}: {sum(list(range(x,y+1,2)))}")