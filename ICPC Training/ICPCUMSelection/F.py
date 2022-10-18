# price = [1000, 800, 400, 300, 400, 200]
# imp = [5, 2, 5, 5, 3, 2]
# val = [a*b for a, b in zip(price, imp)]
# N = 1000


def decision(price, imp, val, N, i):
    if i == (len(price) - 1):
        if N > price[i]:
            return val[i]
        else:
            return 0
    if N > price[i]:
        return max(decision(price, imp, val, N, i+1), val[i] + decision(price, imp, val, N - price[i], i+1))
    else:
        return decision(price, imp, val, N, i+1)


N, n = [int(x) for x in input().strip().split()]
DP = [[-1 for i in range(N+1)] for j in range(int(N+1))]

price = []
imp = []

for i in range(n):
    a, b = [int(x) for x in input().strip().split() if x != ""]
    price.append(a)
    imp.append(b)

val = [a*b for a, b in zip(price, imp)]

print(decision(price, imp, val, N, 0))




####################################################################################################################
# # price = [1000, 800, 400, 300, 400, 200]
# # imp = [5, 2, 5, 5, 3, 2]
# # val = [a*b for a, b in zip(price, imp)]
# # N = 1000


# def decision(price, imp, val, N, i,dp):
# 	if dp[N][i] != -1:
# 		return dp[N][i]
# 	if i == (len(price) - 1):
# 		if N > price[i]:
# 			dp[N][i] = val[i]
# 			return dp[N][i]
# 		else:
# 			return 0
# 	if N > price[i]:
# 		dp[N][i] = max(decision(price, imp, val, N, i,dp+1), val[i] + decision(price, imp, val, N - price,dp[i], i+1))
# 		return dp[N][i]
# 	else:
# 		dp[N][i] =  decision(price, imp, val, N, i,dp+1)
# 		return dp[N][i]


# N, n = [int(x) for x in input().strip().split()]
# DP = [[-1 for i in range(N+1)] for j in range(int(N+1))]
# price = []
# imp = []

# for i in range(n):
# 	a, b = [int(x) for x in input().strip().split() if x != ""]
# 	price.append(a)
# 	imp.append(b)

# val = [a*b for a, b in zip(price, imp)]

# print(price, imp, val, N)
# print(decision(price, imp, val, N, 0,DP))




# 1000 5
# 800 2
# 400 5
# 300 5
# 400 3
# 200 2