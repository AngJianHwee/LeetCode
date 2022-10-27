x = int(input().strip())
for i in range(x, 1000000000+1):
	if i%sum([int(i_) for i_ in str(i)]) == 0:
		print(i)
		break