# # v1: Iter
# b = 0
# input()
# a = [float(x) for x in input().split()]
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         b += sum(a[i:j+1])
# print(f"{b:.2f}")


# # v2: better iter
# input()
# a = [float(x) for x in input().split()]
# b = 0

# for i in range(1,len(a)+ 1):
# 	s = None
# 	for j in range(len(a)):
# 		if j+i > len(a):
# 			break
# 		if s is None:
# 			s = sum(a[j:j+i])
# 		else:
# 			s += a[j+i-1]
# 			s -= a[j-1]
# 		b += s
# print(f"{b:.2f}")


# v3: dp
# a = [float(x) for x in input().split()]
a = [0.1, 0.2, 0.3, 0.4]
c = [[-1 for j in range(len(a))] for i in range(len(a))]
def dp(a,i,j,c):
	if c[i][j] != -1:
		return c[i][j]
	else:
		if i == j:
			c[i][j] = a[i]
		else:
			c[i][j] = a[i] + dp(a,i+1,j,c)
		return c[i][j]
for i in range(len(a)):
	dp(a,0,i,c)
print(c)