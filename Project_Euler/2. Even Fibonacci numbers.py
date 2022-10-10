fib = [1,2]
while fib[-1] < int(4e6):
	fib.append(fib[-1] + fib[-2])
print(sum([x for x in fib if x%2 == 0]))
