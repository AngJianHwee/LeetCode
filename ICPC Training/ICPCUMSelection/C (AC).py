def calcSum(string):
	sc = []
	cs = 0
	for s in string:
		if s == 'O':
			cs += 1
		else:
			cs = 0
		sc.append(cs)
	return sum(sc)

for i in range(int(input())):
	s = input()
	print(calcSum(s))


# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
