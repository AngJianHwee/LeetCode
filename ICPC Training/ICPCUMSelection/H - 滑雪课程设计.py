
def cost(arr, l, u):
    return sum([abs(x-l)**2 for x in arr if x < l])+sum([abs(x-u)**2 for x in arr if x > u])


arr = []
for i in range(int(input())):
    arr.append(int(input().strip()))
# print(arr)

if max(arr) - min(arr) < 17:
    print(0)
else:
    start = min(arr)
    l = min(arr)
    u = max(arr)-17
    print(min([cost(arr, i, i+17) for i in range(l, u+1)]))


# 33
# def cost(arr,l,u):
# 	return sum([abs(x-l)**2 for x in arr if x<l])+sum([abs(x-u)**2 for x in arr if x>u])

# arr = [20, 4, 1, 24, 21]
# if max(arr) - min(arr) < 17:
#     print(0)
# else:
# 	start = min(arr)
# 	l = min(arr)
# 	u = max(arr)-17
# # 	while (u - l) > 10:
# # 		m = (l+u)//2+l
# # 		if cost(arr,l,l+17)-cost(arr,m,m+17)>cost(arr,u,u+17)-cost(arr,m,m+17):
# # 			l = m
# # 			# u = m
# # 		else:
# # 			u = m
# # 			# l = m
# 	print(min([cost(arr,i,i+17) for i in range(l,u+1)]))


# # # diff = max(arr) - min(arr) - 17
# # # for j in range(1, diff):
# # #     print(j,[x for x in arr if (x >= (max(arr) - j))
# # #            or (x <= (min(arr) + (diff - j)))])
# # #     # c.append(cost(arr,j,diff))


# # # 5
# # # 20
# # # 4
# # # 1
# # # 24
# # # 21
