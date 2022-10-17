from typing import List

class Solution:
	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
		def find1(mat,i):
			if mat[i][0] == 0:
				return 0
			if mat[i][-1] == 1:
				return 0
				
			if mat[i][0] == 1 and mat[1] == 0:
				return 1

			l,r = 0,len(mat[i])-1
			while l < r:
				if l == r-1:
					if mat[i][l] == 1:
						return l
					return r
				m = l + (r-l)//2
				print(mat[i],l,m,r,mat[i][m])
				if mat[i][m] == 0:
					r = m
				else:
					l = m
			return l+1

		x = sorted([f"{find1(mat, i)}{i:05d}"  for i in range(len(mat))])
		return [int(x_[-4:]) for x_ in x][:k]


s = Solution()
print(s.kWeakestRows(mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], k = 3))
print(s.kWeakestRows(mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], k = 2))
print(s.kWeakestRows([[1,0],[0,0],[1,0]],2))
print(s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))