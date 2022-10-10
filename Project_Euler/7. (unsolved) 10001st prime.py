# def prime(lower, upper):
# 	primes = []
# 	for num in range(lower, upper + 1):
# 	   # all prime numbers are greater than 1
# 	   if num > 1:
# 		   for i in range(2, num):
# 			   if (num % i) == 0:
# 				   break
# 		   else:
# 			   primes.append(num)
# 	return primes

# primes = []
# target = 10001

# for i in range(2, int(1e10), 100):
# 	if len(primes)> target:
# 		print(primes[target-1])
# 		break
# 	primes.extend(prime(i, i+100))