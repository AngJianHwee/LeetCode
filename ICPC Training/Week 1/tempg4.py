def longestCommonSubsequence(arr1: str, arr2: str) -> int:
    dpr = [[-1 for i in range(max(len(arr1), len(arr2))+1)] for j in range(max(len(arr1), len(arr2))+1)]
    def dp(s1,s2,p1,p2, dpr):
        if dpr[p1][p2] != -1:
            return dpr[p1][p2]
        if p1 == len(s1) or p2 == len(s2):
            dpr[p1][p2] = 0
            return 0
        if s1[p1] == s2[p2]:
            dpr[p1][p2] = 1 + dp(s1,s2,p1+1,p2+1,dpr)
            return dpr[p1][p2]
        else:
            dpr[p1][p2] = max(dp(s1,s2,p1+1,p2,dpr),dp(s1,s2,p1,p2+1,dpr))
            return dpr[p1][p2]
    return dp(arr1,arr2,0,0,dpr)


for i in range(int(input())):
	input()
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]

	b_new = []
	for b_ in b:
		try:
			x = a.index(b_)
		except:
			x = -1
		b_new.append(x)
	# LIS is longest common subsequence between the two arrays
	# print(b_new)
	# print(sorted(b_new))

	print(f"Case {i+1}: {longestCommonSubsequence(b_new,sorted(b_new))}")

