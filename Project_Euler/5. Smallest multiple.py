def divisible(num):
	for i in range(15,1,-1):
			if (num % i) != 0:
				return False
	else:
		return True

for num in range(20,int(1e8)):
	if divisible(num):
		print(num)
		break