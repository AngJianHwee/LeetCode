# m, n = [int(x) for x in input().strip().split()]
# arr = [[-1 for i in range(m-n)] for j in range(int(m-n))]

def BFS(s,e,arr):
	


print(BFS(1, 3, [[0, 1, 0],
				 [1, 0, 1],
				 [0, 1, 0]], []))
######################################### SAMPLE INPUT ##################################
# def count(m,n):
# 	if m < 0:
# 		return int(-1e3)
# 	if m == n:
# 		return 1
# 	if m > int(1e5):
# 		return int(-1e3)
# 	return 1 + max(count(m*2, n),count(m - 1,n))

# print(count(4,6))
