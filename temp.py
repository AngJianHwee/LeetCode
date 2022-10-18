# from typing import List


# class Solution:
#     def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
#         dic = {}
#         for x, y in logs:
#             try:
#                 dic[x] = min(y, dic[x])
#             except:
#                 dic[x] = y

#         arr = [0 for i in range(k)]
#         for x,y in dic.items():
#             arr[y-1] += 1
#         return arr


# s = Solution()
# print(s.findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))
# print(s.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4))
# # # Model Solution



X = [-0.15, 8.6, 5.0, 3.71, 4.29, 7.74, 2.48, 3.25, -1.15, 8.38]
Y = [2.55, 12.07, 0.46, 0.35, 2.69, -0.94, 1.73, 0.73, -0.35, -0.37]
print(sorted(X))
print(sorted(Y))
print(sorted(X+Y))



# Python program for KMP Algorithm
def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)

	# create lps[] that will hold the longest prefix suffix
	# values for pattern
	lps = [0]*M
	j = 0 # index for pat[]

	# Preprocess the pattern (calculate lps[] array)
	computeLPSArray(pat, M, lps)

	i = 0 # index for txt[]
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			print ("Found pattern at index", str(i-j))
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain
