arr = [int(x) for x in input().strip().split()]
l = 0
s = 0
for x in arr:
	if x > l:
		s += 6*(x-l)	
	else:
		s += 4*(l-x)
	l = x
	s += 5
print(s)