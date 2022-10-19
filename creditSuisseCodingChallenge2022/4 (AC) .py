# n = ["Alice", "Bob", "Cacey", "Deepak", "Emma"]
# s = [10, 11, 10, 12, 14]
# e = [14, 12, 15, 16, 16]

# n = ["Neil","Angel","Alok"]
# s = [1,7,7]
# e = [10,9,10]

# n = ["Alice","Bob"]
# s = [1,5]
# e = [3,7]

def solution(m, employees, shifts):

	n = employees
	s = [x[0] for x in shifts]
	e = [x[1] for x in shifts]

	st = min(s)
	et = max(e)

	x = [[] for i in range(st, et+1)]
	for i in range(len(s)):
		x[s[i]-st].append(i)
		x[e[i]-st].append(i)

	stk = []
	stk_prev = []
	arr = []
	for i in range(len(x)):
		if i != 0:
			if stk != stk_prev:
				arr.append([st + i-1, st+ i, [n[y] for y in stk]])	
			else:
				arr[-1][1] += 1
		
		stk_prev = stk.copy()

		# Refresh 
		if x[i] != []:
			for x_ in x[i]:
				if x_ in stk:
					stk = [y for y in stk if y != x_]
				else:
					stk.append(x_)

		stk = sorted(stk)

	print(len(arr))
	for x in arr:
		print(x[0], x[1], len(x[2]), " ".join(sorted(x[2])))

	return 0


def main():
	n = int(input())
	employees = input().split(" ")
	shifts = []
	for i in range(n):
		line = input().split(" ")
		shifts.append([int(line[0]), int(line[1])])

	solution(n, employees, shifts)


if __name__ == '__main__':
	main()
	
