num = 600851475143 
primes = []

for i in range(2,num):
    if num < i:
        break
    while num % i == 0:
        primes.append(i)
        num /= i
print(primes)
