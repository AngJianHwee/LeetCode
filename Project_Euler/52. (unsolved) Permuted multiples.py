N = 1e8
for i in range(6, int(N)):
	i = 251748
	# if i % 2 != 0:
	# 	continue
	# if i % 3 != 0:
	# 	continue
	# if i % 4 != 0:
	# 	continue
	# if i % 5 != 0:
	# 	continue
	# if i % 6 != 0:
	# 	continue

	# if len(str(i)) != len(str(int(i/6))):
		# continue

	x = [i, i/2, i/3, i/4, i/5, i/6]
	x = ["".join(sorted(str(int(x_)))) for x_ in x]

	# same = 1
	# for j in range(len(x)-1):
	# 	if x[j] != x[j+1]:
	# 		same = 0
	# 		break
	# if not same:
	# 	continue

	print(x)
	break