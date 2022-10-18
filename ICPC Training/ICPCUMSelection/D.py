def longestCommSubseq(s1, s2):
	dp_arr = [[-1 for i in range(max(len(s1), len(s2))+1)] for j in range(max(len(s1), len(s2))+1)]
	
	def dp(s1,s2,p1,p2, dp_arr):
		if dp_arr[p1][p2] != -1:
			return dp_arr[p1][p2]
		if p1 == len(s1) or p2 == len(s2):
			dp_arr[p1][p2] = 0
			return 0
		if s1[p1] == s2[p2]:
			dp_arr[p1][p2] = 1 + dp(s1,s2,p1+1,p2+1,dp_arr)
			return dp_arr[p1][p2]
		else:
			dp_arr[p1][p2] = max(dp(s1,s2,p1+1,p2,dp_arr),dp(s1,s2,p1,p2+1,dp_arr))
			return dp_arr[p1][p2]
	
	return dp(s1,s2,0,0,dp_arr) == len(s1)



while True:
	try:
		[s1,s2] = [str(x) for x in input().strip().split()]
		if longestCommSubseq(s1,s2):
			print("Yes")
		else:
			print("No")
	except :
		break



# print(longestCommSubseq("sequence","subsequence"))
# print(longestCommSubseq("person","compression"))
# print(longestCommSubseq("VERDI","vivaVittorioEmanueleReDiItalia"))
# print(longestCommSubseq("caseDoesMatter","CaseDoesMatter"))


# sequence subsequence
# person compression
# VERDI vivaVittorioEmanueleReDiItalia
# caseDoesMatter CaseDoesMatter




############################################################################################################################################################################################################################

# def isSub(s1,s2,p1,p2):

# 	if s1[p1] == s2[p2]:
# 		p1 += 1
# 		p2 += 1
# 		return isSub(s1,s2,p1,p2)
# 	else:
# 		return isSub(s1,s2,p1+1,p2) or isSub(s1,s2,p1,p2+1)

# print(isSub("abc","abc",0,0))
# # while True:
# # 	try:
# # 	    s1,s2 = [str(x) for x in input().strip().split()]

# # 	except EOFError:

