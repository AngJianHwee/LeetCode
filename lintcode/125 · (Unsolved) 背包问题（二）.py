from typing import (
	List,
)

class Solution:
	"""
	@param m: An integer m denotes the size of a backpack
	@param a: Given n items with size A[i]
	@param v: Given n items with value V[i]
	@return: The maximum value
	"""
	def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
		s = m
		w = a
		v = v
		DP = [[-1 for i in range(int(s+1))] for j in range(int(m+1))]
		def ks(w,v,i,r):
			if DP[i][r] != -1:
				return DP[i][r]

			if i == (len(w)-1):
				if r >= w[i]:
					DP[i][r] = v[i]
					return DP[i][r]
				else:
					return 0
			if r-w[i] >= 0:
				DP[i][r] = max(ks(w,v,i+1,r), (ks(w,v,i+1,r-w[i]) + v[i]))
				return DP[i][r]
			else:
				DP[i][r] = ks(w,v,i+1,r)
				return DP[i][r]

		return ks(w,v,0,s)

s = Solution()
print(s.back_pack_i_i(100,[77,22,29,50,99],[92,22,87,46,90]))

# # Model
# from typing import (
# 	List,
# )

# class Solution:
# 	# @param m: An integer m denotes the size of a backpack
# 	# @param A & V: Given n items with size A[i] and value V[i]
# 	def backPackII(self, m, a, v):
# 		# write your code here
# 		f = [0 for i in range(m+1)]
# 		n = len(a)
# 		for i in range(n):
# 			for j in range(m, a[i]-1, -1):
# 				f[j] = max(f[j] , f[j-a[i]] + v[i])
# 		return f[m]

# s = Solution()
# print(s.backPackII(100,[77,22,29,50,99],[92,22,87,46,90]))

