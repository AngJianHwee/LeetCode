sq_of_sum = 0
sum_of_sq = 0

for i in range(1,100+1):
	sq_of_sum += i
	sum_of_sq += i**2

sq_of_sum = sq_of_sum**2
print(abs(sq_of_sum - sum_of_sq))