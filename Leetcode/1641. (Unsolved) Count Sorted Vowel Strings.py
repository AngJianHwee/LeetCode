from typing import List

class Solution:
	def countVowelStrings(self, n: int) -> int:
		A = [[1,1,1,1,1]]
		for i in range(1,n):
			A_ = []
			for j in range(5):
				A_.append(sum(A[-1][:j+1]))
			A.append(A_[::-1])
		return sum(A[-1])


s = Solution()
print(s.countVowelStrings(n = 1))
print(s.countVowelStrings(n = 2))
print(s.countVowelStrings(n = 33))
