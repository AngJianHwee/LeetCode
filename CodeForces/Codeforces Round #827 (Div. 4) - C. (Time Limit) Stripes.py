for i in range(int(input())):
	input()
	input()
	arr = []
	for _ in range(8):
		arr.append([x for x in input().strip()])

	done = False
	for x in arr:
		if len(set(x)) == 1:
			if x[0] != ".":
				print(x[0])
				done = True
				break

	if done:
		continue


	for i in range(len(arr[0])-1):
		arr2 = [x[i] for x in arr]
		if len(set(arr2)) == 1:
			if arr2[0] != ".":
				print(arr2[0])
				break




# 4


# ....B...
# ....B...
# ....B...
# RRRRRRRR
# ....B...
# ....B...
# ....B...
# ....B...


# RRRRRRRB
# B......B
# B......B
# B......B
# B......B
# B......B
# B......B
# RRRRRRRB


# RRRRRRBB
# .B.B..BB
# RRRRRRBB
# .B.B..BB
# .B.B..BB
# RRRRRRBB
# .B.B..BB
# .B.B..BB


# ........
# ........
# ........
# RRRRRRRR
# ........
# ........
# ........
# ........